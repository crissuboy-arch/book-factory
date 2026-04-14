"""
Gera capa + ilustrações via DALL-E 3 e exporta o livro em PDF diagramado.

Uso:
    python export_pdf.py --manuscript examples/amor-blindado/manuscrito.md
"""

import os
import re
import sys
import argparse
import requests
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from fpdf import FPDF
from PIL import Image

# ── Configuração ──────────────────────────────────────────────────────────────

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    sys.exit("Erro: OPENAI_API_KEY não encontrada no arquivo .env")

client = OpenAI(api_key=api_key)

# ── Geração de imagens ────────────────────────────────────────────────────────

def gerar_imagem(prompt: str, dest: Path, size: str = "1024x1792") -> Path:
    """Chama DALL-E 3 e salva como JPEG. Pula se já existir."""
    jpeg = dest.with_suffix(".jpg")
    if jpeg.exists():
        print(f"    (já existe, pulando) {jpeg.name}")
        return jpeg

    print(f"    Chamando DALL-E 3 para: {dest.name}...")
    try:
        resp = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="hd",
            n=1,
        )
        url = resp.data[0].url
        raw = requests.get(url, timeout=60).content
        dest.write_bytes(raw)
        img = Image.open(dest).convert("RGB")
        img.save(jpeg, "JPEG", quality=90)
        dest.unlink()
        return jpeg
    except Exception as e:
        print(f"    AVISO: falha ao gerar imagem — {e}")
        return None


# ── Parser do manuscrito ──────────────────────────────────────────────────────

def limpar_inline(text: str) -> str:
    """Remove marcações markdown inline."""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    # Aspas tipográficas → aspas simples para evitar encoding issues
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    text = text.replace('\u2014', '-').replace('\u2013', '-')
    return text.strip()


def parse_manuscrito(path: Path):
    """
    Lê o manuscrito e retorna (meta, capítulos).
    Cada capítulo tem: number, title, image_desc, body_blocks (lista de blocos).
    Bloco: {"type": "heading"|"bullet"|"paragraph", "text": str}
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    meta = {"genre": "autoajuda"}
    chapters = []
    current_ch = None
    current_body_lines = []
    current_section = None

    for line in lines:
        # Título do livro (# nível 1)
        if re.match(r"^# [^#]", line) and "title" not in meta:
            parts = line[2:].split(":", 1)
            meta["title"] = parts[0].strip()
            if len(parts) > 1:
                meta["subtitle"] = parts[1].strip()
            current_section = None
            continue

        # Seções especiais de nível ##
        if re.match(r"^## Subtítulo", line, re.IGNORECASE):
            current_section = "subtitle"
            continue
        if re.match(r"^## Sinopse", line, re.IGNORECASE):
            current_section = "synopsis"
            continue
        if re.match(r"^## Biografia", line, re.IGNORECASE):
            current_section = "bio"
            continue
        if re.match(r"^## (Índice|Indice)", line, re.IGNORECASE):
            current_section = "index"
            continue
        if re.match(r"^## Pontuação", line, re.IGNORECASE):
            current_section = "ignore"
            continue
        if re.match(r"^## Formatação", line, re.IGNORECASE):
            current_section = "ignore"
            continue

        # Capítulos (## nível 2)
        m_cap = re.match(r"^## (Capítulo|Chapter)\s+(\d+)[:\-–]?\s*(.*)", line, re.IGNORECASE)
        if m_cap:
            # Fecha capítulo anterior
            if current_ch is not None:
                current_ch["body_blocks"] = _build_blocks(current_body_lines)
                chapters.append(current_ch)
            current_ch = {
                "number": int(m_cap.group(2)),
                "title": limpar_inline(m_cap.group(3).strip()),
                "image_desc": "",
            }
            current_body_lines = []
            current_section = "chapter"
            continue

        # Acumula conteúdo conforme a seção
        if current_section == "subtitle" and line.strip():
            meta["subtitle"] = meta.get("subtitle", "") + line.strip()
        elif current_section == "bio" and line.strip():
            if "author" not in meta:
                words = line.strip().split()
                meta["author"] = " ".join(words[:2]) if len(words) >= 2 else words[0]
        elif current_section == "chapter":
            # Detecta início de descrição de imagem — captura e para de acumular no body
            if re.match(r"^### Descrição de imagem", line, re.IGNORECASE):
                current_section = "image_desc"
                continue
            current_body_lines.append(line)
        elif current_section == "image_desc":
            if line.strip():
                current_ch["image_desc"] += line.strip() + " "

    # Fecha último capítulo
    if current_ch is not None:
        current_ch["body_blocks"] = _build_blocks(current_body_lines)
        chapters.append(current_ch)

    return meta, chapters


def _build_blocks(lines: list) -> list:
    """
    Converte linhas brutas do corpo do capítulo em blocos tipados.
    Tipos: heading (### nível 3), bullet (- item), paragraph (texto corrido)
    """
    blocks = []
    for line in lines:
        raw = line.strip()
        if not raw:
            continue
        # Heading ### (Introdução, Desenvolvimento, Conclusão, etc.)
        m_h = re.match(r"^#{1,4}\s+(.+)", raw)
        if m_h:
            blocks.append({"type": "heading", "text": limpar_inline(m_h.group(1))})
            continue
        # Bullet point
        m_b = re.match(r"^[-•]\s+(.*)", raw)
        if m_b:
            blocks.append({"type": "bullet", "text": limpar_inline(m_b.group(1))})
            continue
        # Parágrafo normal
        blocks.append({"type": "paragraph", "text": limpar_inline(raw)})

    return blocks


# ── Construção do PDF ─────────────────────────────────────────────────────────

# Fontes Unicode (Arial do Windows suporta português completo)
_FONT_DIR = Path("C:/Windows/Fonts")
_USE_UNICODE = (_FONT_DIR / "arial.ttf").exists()


class LivroPDF(FPDF):
    def __init__(self, titulo, autor):
        super().__init__(orientation="P", unit="mm", format=(148, 210))
        self.livro_titulo = titulo
        self.livro_autor = autor
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 18, 18)
        if _USE_UNICODE:
            self.add_font("Arial", "",  str(_FONT_DIR / "arial.ttf"))
            self.add_font("Arial", "B", str(_FONT_DIR / "arialbd.ttf"))
            self.add_font("Arial", "I", str(_FONT_DIR / "ariali.ttf"))
            self.add_font("Arial", "BI", str(_FONT_DIR / "arialbi.ttf"))
            self._fn = "Arial"
        else:
            self._fn = "Helvetica"

    def _font(self, style="", size=10):
        self.set_font(self._fn, style, size)

    def _w(self):
        """Largura útil considerando margens."""
        return self.w - self.l_margin - self.r_margin

    def header(self):
        if self.page_no() > 1:
            self._font("I", 7)
            self.set_text_color(150)
            self.set_x(self.l_margin)
            self.cell(self._w(), 5, f"{self.livro_titulo}  |  {self.livro_autor}", align="C")
            self.ln(4)
            self.set_text_color(0)

    def footer(self):
        self.set_y(-14)
        self._font("I", 8)
        self.set_text_color(150)
        self.cell(0, 8, str(self.page_no()), align="C")
        self.set_text_color(0)

    def pagina_capa(self, img_path, titulo, subtitulo, autor):
        self.add_page()
        tem_imagem = img_path and Path(img_path).exists()
        if tem_imagem:
            self.image(str(img_path), x=0, y=0, w=self.w, h=self.h)
        # Repõe margens e posição após imagem full-page
        self.set_margins(18, 18, 18)
        self.set_xy(self.l_margin, 22)
        w_util = self._w()
        cor_texto = (255, 255, 255) if tem_imagem else (20, 20, 60)
        self.set_text_color(*cor_texto)
        # Título
        self._font("B", 22)
        self.multi_cell(w_util, 11, titulo, align="C")
        # Subtítulo
        if subtitulo:
            sub = subtitulo.split(".")[0].strip()
            self._font("I", 11)
            self.set_x(self.l_margin)
            self.multi_cell(w_util, 6, sub, align="C")
        # Autor na base
        self.set_xy(self.l_margin, self.h - 22)
        self._font("B", 12)
        self.cell(w_util, 8, autor, align="C")
        self.set_text_color(0)

    def pagina_capitulo(self, numero, titulo, body_blocks, img_path):
        self.add_page()
        w = self._w()

        # ── Cabeçalho do capítulo ──────────────────────────────────────────
        self._font("B", 13)
        self.set_text_color(30, 30, 100)
        self.set_x(self.l_margin)
        self.multi_cell(w, 7, f"Capítulo {numero}", align="C")
        self.ln(1)
        self._font("B", 11)
        self.set_x(self.l_margin)
        self.multi_cell(w, 6, titulo, align="C")
        self.set_text_color(0)

        # Linha decorativa abaixo do título
        self.ln(3)
        x_start = self.l_margin + w * 0.25
        self.set_draw_color(30, 30, 100)
        self.set_line_width(0.4)
        self.line(x_start, self.get_y(), x_start + w * 0.5, self.get_y())
        self.ln(5)

        # ── Ilustração ─────────────────────────────────────────────────────
        if img_path and Path(img_path).exists():
            self.image(str(img_path), x=self.l_margin, w=w)
            self.ln(5)

        # ── Blocos de conteúdo ──────────────────────────────────────────────
        for block in body_blocks:
            btype = block["type"]
            text  = block["text"]

            if btype == "heading":
                self.ln(3)
                self._font("B", 10)
                self.set_text_color(30, 30, 100)
                self.set_x(self.l_margin)
                self.multi_cell(w, 6, text.upper())
                self.set_text_color(0)
                self.ln(1)

            elif btype == "bullet":
                self._font("", 10)
                # Indenta bullet em 5 mm, reduz largura correspondente
                self.set_x(self.l_margin + 5)
                self.multi_cell(w - 5, 5.5, f"\u2022  {text}")
                self.ln(0.5)

            else:  # paragraph
                self._font("", 10)
                self.set_x(self.l_margin)
                self.multi_cell(w, 5.8, text)
                self.ln(2.5)


# ── Pipeline principal ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Exporta manuscrito para PDF com imagens DALL-E 3")
    parser.add_argument("--manuscript", default="examples/amor-blindado/manuscrito.md",
                        help="Caminho para o manuscrito.md")
    args = parser.parse_args()

    manuscrito = Path(args.manuscript)
    if not manuscrito.exists():
        sys.exit(f"Arquivo não encontrado: {manuscrito}")

    saida_dir   = manuscrito.parent / "output"
    imagens_dir = saida_dir / "images"
    saida_dir.mkdir(exist_ok=True)
    imagens_dir.mkdir(exist_ok=True)

    print(f"\nLendo manuscrito: {manuscrito}")
    meta, capitulos = parse_manuscrito(manuscrito)

    titulo    = meta.get("title", "Sem Título")
    subtitulo = meta.get("subtitle", "")
    autor     = meta.get("author", "Autor")

    print(f"Livro: {titulo}")
    print(f"Autor: {autor}")
    print(f"Capítulos encontrados: {len(capitulos)}\n")

    # ── 1. Capa ──────────────────────────────────────────────────────────────
    print("[ 1/3 ] Gerando capa...")
    prompt_capa = (
        f"Professional book cover for a self-help book titled '{titulo}' by {autor}. "
        f"Subtitle: '{subtitulo}'. "
        "Style: warm, modern, Brazilian aesthetic, inspirational. "
        "Elegant typography space at top for title, bottom for author name. "
        "Publishing quality. No text or letters anywhere in the image."
    )
    capa_path = gerar_imagem(prompt_capa, imagens_dir / "cover.png", size="1024x1792")

    # ── 2. Ilustrações de capítulos ───────────────────────────────────────────
    print(f"\n[ 2/3 ] Gerando {len(capitulos)} ilustrações de capítulos...")
    for cap in capitulos:
        desc = cap["image_desc"] or f"Cena do capítulo {cap['number']}: {cap['title']}"
        prompt_cap = (
            f"Book illustration for a Brazilian self-help book, chapter {cap['number']}: "
            f"'{cap['title']}'. Scene: {desc} "
            "Warm realistic style, publishing quality. No text."
        )
        img = gerar_imagem(
            prompt_cap,
            imagens_dir / f"chapter_{cap['number']}.png",
            size="1792x1024",
        )
        cap["img_path"] = img

    # ── 3. Montar PDF ─────────────────────────────────────────────────────────
    print("\n[ 3/3 ] Montando PDF...")
    pdf = LivroPDF(titulo, autor)
    pdf.pagina_capa(capa_path, titulo, subtitulo, autor)

    for cap in capitulos:
        pdf.pagina_capitulo(
            cap["number"],
            cap["title"],
            cap["body_blocks"],
            cap.get("img_path"),
        )

    nome_pdf = re.sub(r"[^\w\-]", "_", titulo) + ".pdf"
    pdf_path = saida_dir / nome_pdf
    pdf.output(str(pdf_path))

    print(f"\nPDF gerado com sucesso:")
    print(f"  {pdf_path.resolve()}\n")


if __name__ == "__main__":
    main()
