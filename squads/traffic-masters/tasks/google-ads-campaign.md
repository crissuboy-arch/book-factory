# Task: Campanha Google Ads

## Objetivo
Criar uma campanha completa no Google Ads — Search e/ou YouTube — para capturar intenção de compra e fazer remarketing.

## Inputs Necessários
```
produto: [nome e preço]
keywords_principais: [termos que o avatar pesquisa]
budget_diario: [R$X]
objetivo: [leads / vendas]
landing_page: [URL]
tag_google_instalada: [sim/não]
conversoes_configuradas: [sim/não]
concorrentes: [nomes para monitorar]
```

## Estrutura Search

### Keyword Research
Para cada tema, listar:
```
Intenção de COMPRA (maior prioridade):
- "comprar [produto]"
- "[produto] preço"
- "[produto] funciona"
- "[produto] vale a pena"

Intenção de PROBLEMA (média prioridade):
- "como [resolver problema]"
- "o que fazer quando [dor]"
- "melhor [solução] para [dor]"

Intenção INFORMACIONAL (baixa prioridade — apenas se tiver orçamento):
- "o que é [categoria]"
- "[categoria] para iniciantes"
```

### Negative Keywords (Obrigatórios)
```
grátis, gratuito, de graça, download grátis
pirata, torrent, crackeado
emprego, salário, concurso
[competitor keywords que não quer pagar]
```

### Estrutura de Ad Groups
```
Campanha: [Produto] - Search - BR
Budget: R$[X]/dia
Estratégia de lance: Maximizar conversões (após 50 conversões) ou CPC Manual (início)

Ad Group 1: Intenção de Compra
  Keywords: [lista phrase match]
  RSA: [3 headlines + 2 descriptions]
  
Ad Group 2: Problema/Solução  
  Keywords: [lista phrase match]
  RSA: [3 headlines + 2 descriptions]
  
Ad Group 3: Marca (proteger)
  Keywords: [nome da marca exact match]
  RSA: [específico para quem já conhece]
```

### Template de RSA
```
Headline 1: [Benefício principal — 30 chars]
Headline 2: [Prova social ou número — 30 chars]
Headline 3: [CTA + urgência — 30 chars]
Headline 4: [Garantia — 30 chars]
Headline 5: [Diferencial — 30 chars]

Description 1: [Benefício + CTA — 90 chars]
Description 2: [Garantia + CTA — 90 chars]
```

## Estrutura YouTube

### Campanha In-Stream Skippable
```
Campanha: [Produto] - YouTube - Awareness/Remarketing
Formato: In-Stream skippable (pular após 5s)
Budget: R$[X]/dia
Audiência: [Interesses + Intenção de compra customizada]

Roteiro do anúncio (30-60s):
0-5s: HOOK (não skippável) — o que faz o usuário querer continuar
5-15s: Identificação do problema
15-30s: Apresentação da solução + credencial
30-45s: Prova + oferta
45-60s: CTA claro e repetido
```

### Remarketing YouTube
Para quem visitou a LP mas não comprou:
- Formato: bumper 6s (não pulável)
- Mensagem: lembrança do benefício + urgência

## Output Esperado
- Lista de keywords organizadas por grupo de intenção
- Lista de negative keywords
- Estrutura completa de campanhas
- 3 RSAs completos (Search)
- Roteiro de vídeo YouTube (30s e 60s)
- Checklist de configuração: tag, conversões, UTMs, link da landing page
