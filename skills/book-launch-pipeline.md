# Skill: Book Launch Pipeline

## Descricao
Pipeline completo que integra o book-factory com todos os squads do xQuads para transformar um manuscrito em um lançamento completo na Hotmart: página de vendas, emails de lançamento e estratégia de tráfego, tudo gerado automaticamente.

## Comando
```
/book-launch manuscript="[caminho/manuscrito.md]" preco="R$[X]" budget_ads="R$[X]"
```

## O que é Gerado Automaticamente

### 1. Do book-factory (já existente)
- Manuscrito completo em markdown
- Capa e ilustrações via DALL-E 3
- PDF diagramado exportado

### 2. Do storytelling squad
- Análise da estrutura narrativa do livro
- Logline irresistível (1 frase para usar em anúncios)
- Mapa de personagens e arco de transformação
- Gancho do livro: a "jornada do leitor"

### 3. Do hormozi-squad
- Grand Slam Offer para a Hotmart
- Definição de preço baseado no ROI do leitor
- Value stack completo (livro + bônus digitais)
- Estrutura de funil: livro → masterclass → mentoria
- Garantia recomendada

### 4. Do brand-squad
- Posicionamento do autor como marca
- Tagline do livro e do autor
- Voz de marca para toda a comunicação

### 5. Do copy-master (principal output)
- **Página de vendas Hotmart** completa (5.000+ palavras)
- **Sequência de 7 emails** de lançamento
- **Script VSL** (10–15 minutos) para o vídeo da página
- **20+ headlines** para testes A/B
- **30+ bullets** de benefícios para a página

### 6. Do traffic-masters
- **Estratégia de tráfego** (Meta + Google + orgânico)
- **5 anúncios prontos** para Meta Ads (copy + briefing visual)
- **Campanha Google Search** (keywords + RSAs)
- **Roteiro de Reels/TikTok** (5 vídeos de conteúdo para lançamento)
- **Calendário editorial** de 30 dias (orgânico)

## Processo de Execucao

### FASE 1: Analise do Manuscrito (storytelling)

```markdown
Inputs lidos automaticamente do manuscrito.md:
- Título e subtítulo
- Sinopse
- Autor e biografia
- Capítulos e descrições de imagens
- Gênero e tema

Output:
- logline.md
- reader-journey.md (jornada do leitor como herói)
```

### FASE 2: Construcao da Oferta (hormozi-squad)

```markdown
Inputs:
- Título, subtítulo, sinopse (do manuscrito)
- Preco desejado (do comando)
- Público-alvo identificado

Output: offer-stack.md
│
│ Exemplo para "Amor Blindado" (R$47):
│ ✓ eBook "Amor Blindado" — Valor: R$197
│ ✓ Workbook de Exercícios Práticos — Valor: R$97
│ ✓ Checklist "30 Dias de Amor Blindado" — Valor: R$47
│ ✓ Acesso ao grupo privado — Valor: R$97
│ TOTAL: R$438 → Você investe: R$47
│ Garantia: 30 dias sem perguntas
```

### FASE 3: Copy Completa (copy-master)

Executa em sequência usando o pipeline do copy-master:

**3a. Headlines** (Ogilvy + Halbert)
Gera 20 headlines a partir do título, logline e promessa do livro.
Seleciona top 5 para teste.

**3b. Página de Vendas Hotmart** (Kennedy + Brunson + Hormozi + Cialdini)
Estrutura completa seguindo o template de `tasks/sales-page.md`.
Inputs automáticos:
- Hero: o leitor (não o autor)
- Problema: o que o livro resolve
- Mecanismo: o método do livro
- Oferta: o value stack criado na Fase 2
- Prova: depoimentos placeholder + estatísticas do nicho

**3c. Sequência de 7 Emails** (Kennedy + Brunson)
Usando o template de `tasks/launch-email.md`.
D-7 ao D-Day com histórias do livro.

**3d. Script VSL** (Brunson + Halbert + Hormozi)
Script completo para o vídeo da página de vendas.
Usa a logline e a jornada do leitor como herói.

### FASE 4: Trafego (traffic-masters)

**4a. Meta Ads**
- 3 ad sets (Advantage+, Interesses, Retargeting)
- 5 variações de copy
- Briefing para 3 criativos (vídeo 30s, imagem, carrossel)

**4b. Google Ads**
- Keywords do nicho do livro (intenção de compra)
- 3 RSAs otimizados
- Negative keywords

**4c. Conteúdo Orgânico**
- 5 scripts de Reels baseados nos capítulos do livro
- 30 posts para Instagram/LinkedIn (calendário de lançamento)
- 5 ideias de vídeo para YouTube

## Estrutura de Output

```
[pasta-do-livro]/
├── manuscrito.md          (gerado pelo book-factory)
├── output/
│   ├── [Titulo].pdf       (gerado pelo export_pdf.py)
│   └── images/            (capa + ilustrações DALL-E)
└── launch/
    ├── offer-stack.md           (Fase 2 — Hormozi)
    ├── positioning.md           (Fase 2 — Brand)
    ├── logline.md               (Fase 1 — Storytelling)
    ├── copy/
    │   ├── headlines.md         (20+ headlines)
    │   ├── sales-page-hotmart.md  (página de vendas completa)
    │   ├── email-sequence/
    │   │   ├── email-1.md
    │   │   ├── email-2.md
    │   │   ├── email-3.md
    │   │   ├── email-4.md
    │   │   ├── email-5.md
    │   │   ├── email-6.md
    │   │   └── email-7.md
    │   ├── vsl-script.md        (script do vídeo)
    │   └── bullets.md           (30+ bullets)
    └── traffic/
        ├── meta-ads.md          (estrutura + copy + briefing)
        ├── google-ads.md        (keywords + RSAs)
        ├── reels-scripts.md     (5 roteiros)
        └── content-calendar.md  (30 dias orgânico)
```

## Exemplo de Uso

Para lançar "Amor Blindado" na Hotmart com budget de R$1.500/mês em anúncios:

```
/book-launch manuscript="examples/amor-blindado/manuscrito.md" preco="R$47" budget_ads="R$1500"
```

O sistema irá:
1. Ler o manuscrito e extrair todos os dados automaticamente
2. Criar a oferta Hormozi com value stack + garantia
3. Gerar a página de vendas completa para Hotmart
4. Criar 7 emails de lançamento com histórias do livro
5. Escrever o script VSL de 12 minutos
6. Estruturar a campanha Meta Ads com 5 anúncios prontos
7. Criar a campanha Google Search com keywords do nicho de relacionamento
8. Gerar 5 roteiros de Reels baseados nos capítulos do livro
9. Entregar tudo em `examples/amor-blindado/launch/`

## Notas de Implementacao
- Cada fase pode ser executada individualmente com o comando do squad específico
- O pipeline completo pode levar 20–40 minutos dependendo do tamanho do manuscrito
- Imagens para anúncios precisam ser criadas por designer com base nos briefings gerados
- A página de vendas deve ser revisada pelo criador antes de publicar na Hotmart
- Chave OPENAI_API_KEY necessária no `.env` para geração de imagens (DALL-E 3)
