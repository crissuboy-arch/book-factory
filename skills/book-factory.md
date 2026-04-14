# Book Factory Skill

## Description
A comprehensive skill for generating complete book manuscripts in multiple languages and genres. This skill leverages AI to create fictional or non-fictional content based on user-specified parameters.

## Supported Languages
- Portuguese (pt)
- English (en)
- Spanish (es)
- French (fr)

## Supported Genres
- Romance
- Thriller
- Fantasy
- Self-help
- Short Stories (Contos)

## Commands

### /book-create
Generates a complete book manuscript including title, characters, chapters, and synopsis.

#### Parameters
- `language`: The language of the book (pt, en, es, fr)
- `theme`: The central theme or topic of the book (e.g., "love in the city", "mysterious murder", "magical adventure")
- `genre`: The genre of the book (romance, thriller, fantasy, self-help, short-stories)
- `type`: The type of content (full-book for complete novels, short-story for concise narratives)
- `chapters`: Number of chapters for full-book (10, 20, 30, or 60; ignored for short-story)

#### Output Structure
The generated manuscript will include:
1. **Title**: An engaging title in the specified language
2. **Subtitle**: A complementary subtitle enhancing the title
3. **Cover Synopsis**: A compelling blurb for the book cover (150-250 words)
4. **Author Biography**: A fictional or generated author bio (100-200 words)
5. **Characters**: A list of main characters with brief descriptions
6. **Synopsis**: A detailed summary of the plot
7. **Table of Contents/Index**: Complete list of chapters with page numbers (estimated)
8. **Chapters**: For full-book: The specified number of complete chapters (10, 20, 30, or 60), each with at least 2000 words; for short-story: A single complete narrative
9. **Chapter Image Descriptions**: Detailed descriptions for AI-generated images or illustrations for each chapter
10. **Quality Score**: A rating out of 10 based on originality, coherence, engagement, and adherence to genre conventions
11. **Formatted Files**: Ready-to-upload files formatted for Amazon KDP (EPUB/DOCX) and Hotmart (PDF/EPUB)

#### Usage Example
/book-create language=en theme="a forbidden love story in Victorian England" genre=romance type=full-book chapters=20

## Implementation Details

### Genre-Specific Guidelines
- **Romance**: Focus on emotional connections, conflicts, and happy endings
- **Thriller**: Build suspense, include twists, mystery elements
- **Fantasy**: Incorporate magical elements, world-building, mythical creatures
- **Self-help**: Provide practical advice, motivational content, step-by-step guidance
- **Short Stories**: Concise narratives with clear beginning, middle, and end

### Language Adaptation
- Ensure all generated content is in the specified language
- Use appropriate cultural references and idioms for each language
- Maintain grammatical correctness and natural flow

### Content Quality Standards
- Original, creative content
- Age-appropriate (general audience)
- Respectful and inclusive
- Avoid harmful stereotypes or offensive material

### Generation Process
1. Analyze the theme, genre, and chapter count to determine plot structure and pacing
2. Create compelling characters that fit the theme
3. Develop a coherent storyline with appropriate pacing across the specified number of chapters
4. Generate detailed cover elements: title, subtitle, cover synopsis, author biography
5. Create a complete table of contents with estimated page numbers
6. Write full chapters, each with at least 2000 words, ensuring narrative progression
7. Generate detailed image descriptions for each chapter to aid in visual representation
8. Format the entire manuscript for publication on Amazon KDP and Hotmart
9. Ensure the synopsis captures the essence of the story

### Quality Scoring System
After generating the manuscript, evaluate it on a scale of 1-10 across the following criteria:
- **Originality (1-10)**: How unique and creative the content is
- **Coherence (1-10)**: Logical flow of plot and character development
- **Engagement (1-10)**: Ability to captivate the reader
- **Genre Adherence (1-10)**: How well it fits the chosen genre conventions
- **Overall Score**: Average of the above, with justification for the rating

Provide feedback on strengths and areas for improvement.

## Image Generation with DALL-E 3

### Authentication
Use the environment variable `OPENAI_API_KEY` (defined in `.env` at the project root) to authenticate with the OpenAI API. Never hardcode keys in code or skill files.

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
```

### Book Cover Generation
Generate a professional cover image using DALL-E 3 when the manuscript is complete.

**Prompt template:**
```
Professional book cover for a [GENRE] book titled "[TITLE]" by [AUTHOR].
Subtitle: "[SUBTITLE]".
Style: [cinematic/minimalist/illustrated/painterly] depending on genre.
Include space at the top for the title and at the bottom for the author name.
High resolution, publishing quality, no text in the image itself.
```

**API call:**
```python
def generate_cover(title, author, subtitle, genre):
    style_map = {
        "romance": "painterly, warm tones, romantic atmosphere",
        "thriller": "dark, cinematic, noir style, dramatic lighting",
        "fantasy": "epic illustrated, magical elements, vivid colors",
        "self-help": "clean minimalist, modern design, inspiring",
        "short-stories": "artistic collage, expressive brushwork",
    }
    style = style_map.get(genre, "professional, modern")
    prompt = (
        f"Professional book cover for a {genre} book titled '{title}' by {author}. "
        f"Subtitle: '{subtitle}'. Style: {style}. "
        "High resolution, publishing quality. No text or letters in the image."
    )
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1792",   # portrait — closest to book cover ratio
        quality="hd",
        n=1,
    )
    return response.data[0].url   # download and save as cover.png
```

### Chapter Illustration Generation
Generate one illustration per chapter based on its image description field.

**API call:**
```python
def generate_chapter_image(chapter_number, image_description, genre):
    prompt = (
        f"Book illustration for chapter {chapter_number}. "
        f"{image_description}. "
        f"Genre: {genre}. Artistic, publishing quality, no text."
    )
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",   # landscape — fits inline in PDF
        quality="hd",
        n=1,
    )
    return response.data[0].url   # download and save as chapter_{n}.png
```

### Image Download Helper
```python
import requests
from pathlib import Path

def download_image(url, dest_path: Path):
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    dest_path.write_bytes(resp.content)
```

---

## PDF Export

### Dependencies
```
pip install fpdf2 Pillow requests openai python-dotenv
```

### Full Export Script (`export_pdf.py`)
```python
"""
Exports a book manuscript + DALL-E images to a print-ready PDF.
Run from the project root:
    python export_pdf.py --manuscript examples/my-book/manuscrito.md
"""

import os, argparse, re, textwrap
from pathlib import Path
import requests
from dotenv import load_dotenv
from openai import OpenAI
from fpdf import FPDF
from PIL import Image

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# ── Image generation ──────────────────────────────────────────────────────────

def generate_and_save(prompt: str, dest: Path, size="1024x1792"):
    if dest.exists():
        return   # skip if already generated
    resp = client.images.generate(
        model="dall-e-3", prompt=prompt, size=size, quality="hd", n=1
    )
    url = resp.data[0].url
    raw = requests.get(url, timeout=60).content
    dest.write_bytes(raw)
    # Convert to JPEG for smaller PDF size
    img = Image.open(dest).convert("RGB")
    jpeg_dest = dest.with_suffix(".jpg")
    img.save(jpeg_dest, "JPEG", quality=90)
    dest.unlink()
    return jpeg_dest


# ── PDF builder ───────────────────────────────────────────────────────────────

class BookPDF(FPDF):
    def __init__(self, title, author):
        super().__init__(orientation="P", unit="mm", format="A5")
        self.book_title = title
        self.book_author = author
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120)
            self.cell(0, 6, f"{self.book_title}  |  {self.book_author}", align="C")
            self.ln(4)
            self.set_text_color(0)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120)
        self.cell(0, 10, str(self.page_no()), align="C")
        self.set_text_color(0)

    def add_cover(self, cover_path: Path, title, subtitle, author):
        self.add_page()
        self.image(str(cover_path), x=0, y=0, w=self.w, h=self.h)
        # Overlay title block (semi-transparent rectangle via draw)
        self.set_fill_color(0, 0, 0)
        self.set_alpha = lambda a: None   # fpdf2 does not support alpha natively
        self.set_y(self.h * 0.15)
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(255, 255, 255)
        self.multi_cell(0, 10, title, align="C")
        self.set_font("Helvetica", "I", 13)
        self.multi_cell(0, 7, subtitle, align="C")
        self.set_y(self.h - 30)
        self.set_font("Helvetica", "", 12)
        self.cell(0, 8, author, align="C")
        self.set_text_color(0)

    def add_chapter(self, number, chapter_title, body, image_path: Path | None):
        self.add_page()
        # Chapter heading
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, f"Capítulo {number}: {chapter_title}", ln=True, align="C")
        self.ln(4)
        # Chapter illustration
        if image_path and image_path.exists():
            img_w = self.w - 40
            self.image(str(image_path), x=20, w=img_w)
            self.ln(6)
        # Body text
        self.set_font("Times", "", 11)
        for paragraph in body.split("\n\n"):
            paragraph = paragraph.strip()
            if paragraph:
                self.multi_cell(0, 6, paragraph)
                self.ln(3)


# ── Manuscript parser ─────────────────────────────────────────────────────────

def parse_manuscript(path: Path):
    """Very simple parser — expects H1 for book info, H2 for chapters."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    meta = {}
    chapters = []
    current_chapter = None
    current_body = []

    for line in lines:
        if line.startswith("# ") and not meta.get("title"):
            meta["title"] = line[2:].strip()
        elif line.lower().startswith("autor:") or line.lower().startswith("author:"):
            meta["author"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("subtítulo:") or line.lower().startswith("subtitle:"):
            meta["subtitle"] = line.split(":", 1)[1].strip()
        elif line.lower().startswith("gênero:") or line.lower().startswith("genre:"):
            meta["genre"] = line.split(":", 1)[1].strip()
        elif re.match(r"^## (Capítulo|Chapter)\s+\d+", line, re.IGNORECASE):
            if current_chapter:
                current_chapter["body"] = "\n\n".join(current_body).strip()
                chapters.append(current_chapter)
            m = re.match(r"^## (?:Capítulo|Chapter)\s+(\d+)[:\-–]?\s*(.*)", line, re.IGNORECASE)
            current_chapter = {"number": int(m.group(1)), "title": m.group(2).strip()}
            current_body = []
        elif line.startswith("**Descrição da Imagem") or line.startswith("**Image Description"):
            if current_chapter:
                current_chapter["image_description"] = line.split(":", 1)[-1].strip(" *")
        elif current_chapter is not None:
            current_body.append(line)

    if current_chapter:
        current_chapter["body"] = "\n\n".join(current_body).strip()
        chapters.append(current_chapter)

    return meta, chapters


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manuscript", required=True, help="Path to manuscrito.md")
    args = parser.parse_args()

    manuscript_path = Path(args.manuscript)
    output_dir = manuscript_path.parent / "output"
    output_dir.mkdir(exist_ok=True)
    images_dir = output_dir / "images"
    images_dir.mkdir(exist_ok=True)

    meta, chapters = parse_manuscript(manuscript_path)
    title = meta.get("title", "Sem Título")
    author = meta.get("author", "Autor Desconhecido")
    subtitle = meta.get("subtitle", "")
    genre = meta.get("genre", "fiction").lower()

    print(f"Gerando livro: {title} | {author} | {len(chapters)} capítulos")

    # 1. Generate cover
    print("Gerando capa...")
    cover_path = images_dir / "cover.jpg"
    style_map = {
        "romance": "painterly, warm tones, romantic atmosphere",
        "thriller": "dark cinematic noir, dramatic lighting",
        "fantasy": "epic illustrated, magical elements, vivid colors",
        "self-help": "clean minimalist, modern, inspiring",
    }
    style = style_map.get(genre, "professional, modern")
    cover_prompt = (
        f"Professional book cover for a {genre} novel titled '{title}' by {author}. "
        f"Subtitle: '{subtitle}'. Style: {style}. "
        "Publishing quality. No text or letters anywhere in the image."
    )
    generate_and_save(cover_prompt, images_dir / "cover.png", size="1024x1792")
    cover_path = next(images_dir.glob("cover.*"), None)

    # 2. Generate chapter illustrations
    for ch in chapters:
        img_dest = images_dir / f"chapter_{ch['number']}.png"
        desc = ch.get("image_description", f"Scene from chapter {ch['number']}: {ch['title']}")
        print(f"  Gerando imagem do capítulo {ch['number']}...")
        ch_prompt = (
            f"Book illustration for chapter {ch['number']} titled '{ch['title']}'. "
            f"{desc}. Genre: {genre}. Artistic, publishing quality, no text."
        )
        result = generate_and_save(ch_prompt, img_dest, size="1792x1024")
        ch["image_path"] = result or img_dest.with_suffix(".jpg") if img_dest.with_suffix(".jpg").exists() else None

    # 3. Build PDF
    print("Montando PDF...")
    pdf = BookPDF(title, author)
    if cover_path:
        pdf.add_cover(cover_path, title, subtitle, author)
    for ch in chapters:
        img = ch.get("image_path") or images_dir / f"chapter_{ch['number']}.jpg"
        pdf.add_chapter(ch["number"], ch["title"], ch["body"], img if Path(img).exists() else None)

    pdf_path = output_dir / f"{title.replace(' ', '_')}.pdf"
    pdf.output(str(pdf_path))
    print(f"\nPDF gerado: {pdf_path}")


if __name__ == "__main__":
    main()
```

### Usage
```bash
# Install dependencies
pip install fpdf2 Pillow requests openai python-dotenv

# Generate PDF with cover + chapter images
python export_pdf.py --manuscript examples/romance-magico/manuscrito.md
```

The script will:
1. Parse the manuscript markdown file
2. Generate a professional cover via DALL-E 3 (`output/images/cover.jpg`)
3. Generate one illustration per chapter (`output/images/chapter_N.jpg`)
4. Assemble everything into a print-ready A5 PDF (`output/<Title>.pdf`)

Images already saved to disk are skipped on re-runs to save API credits.

---

## Publication Formatting Instructions

### General Formatting for All Platforms
- **Font and Spacing**: Use 12pt Times New Roman or Garamond for body text, 14pt for chapter titles, 1.5 line spacing, 1-inch margins on all sides.
- **Page Breaks**: Insert page breaks before each chapter, table of contents, and back matter.
- **Headers/Footers**: Include page numbers in footer, book title and author name in header (except first page).
- **Front Matter**: Title page, copyright page, dedication, table of contents, foreword (if applicable).
- **Back Matter**: Author biography, acknowledgments, about the author, other books by author.
- **Images**: Generated automatically via DALL-E 3 using the chapter image description fields (see Image Generation section above).
- **Word Count**: Ensure each chapter meets minimum 2000 words; total book should align with chosen chapter count (e.g., 20 chapters x 2000 words = ~40,000 words minimum).
- **Proofreading**: Run spell check and grammar check in the target language.

### Amazon KDP (Kindle Direct Publishing)
- **File Format**: Export as DOCX for upload, or convert to EPUB using Calibre. Ensure no embedded fonts unless necessary.
- **Cover**: Use the generated cover text elements; design cover with title, subtitle, author name prominently. Dimensions: 2560 x 1600 pixels for full cover.
- **Metadata**: Use cover synopsis as description, add 7 keywords, select BISAC categories matching genre.
- **Pricing**: Base on word count (e.g., 40,000 words ~ $4.99), enroll in KDP Select for wider distribution.
- **Upload Process**: Upload manuscript and cover separately, preview with Kindle Previewer, publish.

### Hotmart
- **File Format**: Export as PDF (print-ready) or EPUB. Embed fonts, ensure high-resolution images.
- **Cover and Description**: Use generated cover synopsis and biography; create eye-catching cover design.
- **Product Page**: Title with subtitle, detailed description using synopsis, author bio in "About the Author" section.
- **Pricing and Sales**: Set price, enable one-time purchase or subscription, set up affiliate commissions.
- **Delivery**: Host files on Hotmart or use external links; provide download instructions.
- **Marketing Tools**: Create bundles, upsells, email sequences, and promotional pages.

Ensure compliance with each platform's content guidelines, including no offensive material and proper copyright notices.
- If an unsupported language is provided, default to English and notify the user
- If the theme is too vague, ask for clarification
- Handle generation failures gracefully with alternative suggestions

## Limitations
- Generated content is for entertainment and inspiration purposes only
- Not intended for commercial use without proper editing and review
- AI-generated content may require human refinement for publication quality