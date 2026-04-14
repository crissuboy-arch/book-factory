# Task: Campanha Meta Ads

## Objetivo
Criar uma campanha completa no Meta Ads Manager — estrutura, segmentação, criativos e copy de anúncio.

## Inputs Necessários
```
produto: [nome e preço]
avatar: [demografico + psicograficos]
budget_diario: [R$X]
objetivo: [leads / compras / tráfego]
landing_page: [URL]
pixel_instalado: [sim/não]
eventos_configurados: [Lead, Purchase, etc.]
prazo_campanha: [data início e fim ou ongoing]
```

## Estrutura Técnica da Campanha

### Configuração
```
Campanha:
  Objetivo: Conversões (Purchase ou Lead)
  Tipo de budget: CBO (Campaign Budget Optimization)
  Budget diário: R$[X]
  Estratégia de lance: Custo por resultado mais baixo (automático)

Ad Set 1 — Advantage+ (Amplo)
  Audience: Advantage+ Shopping Audience ou Broad (18-55)
  Posicionamentos: Automático
  
Ad Set 2 — Interesse (Nicho)
  Audience: Interesses [listar] | Comportamentos [listar]
  Excluir: Compradores recentes (Custom Audience)
  
Ad Set 3 — Retargeting
  Audience: Visitantes da LP (últimos 30 dias) + Engajamento (90 dias)
  Excluir: Compradores
```

## Copy de Anúncio por Formato

### Anúncio de Feed (Imagem ou Video)
```
Texto principal (Primary Text):
[Hook — frase que para o scroll]
[Identificação do problema do avatar]
[Apresentação da solução em 1-2 linhas]
[Prova social rápida]
[CTA com urgência]

Headline: [Benefício principal em até 40 caracteres]
Descrição: [Detalhe da oferta em até 30 caracteres]
CTA button: [Comprar Agora / Saiba Mais / Cadastre-se]
```

### Anúncio de Stories/Reels (Vídeo Vertical 9:16)
```
0-3s: [Hook visual + texto sobreposto — o que faz parar]
3-10s: [Problema identificado]
10-20s: [Solução apresentada]
20-25s: [Prova social (depoimento rápido ou número)]
25-30s: [CTA + oferta]
```

### Carrossel
```
Card 1 (Cover): [Hook que promete o que o carrossel entrega]
Card 2-5: [Conteúdo de valor: dicas, passos, benefícios]
Card Final: [CTA com oferta]
```

## Regras de Copy para Meta

1. **Hook nos primeiros 2 segundos** — texto em vídeo OU primeira linha do caption
2. **Sem "clique aqui"** — Meta proíbe CTAs muito diretos no visual
3. **Texto na imagem**: máximo 20% da área
4. **Emojis estratégicos**: quebram o texto, dirigem o olhar, sem exagero
5. **Uma ação por anúncio**: não pedir seguir E comprar E compartilhar

## Output Esperado
- Estrutura completa da campanha (3 ad sets)
- 5 variações de copy de anúncio (texto principal + headline)
- Briefing de 3 criativos: vídeo (roteiro 30s), imagem (layout), carrossel (5 cards)
- Checklist de configuração técnica (pixel, eventos, UTMs)
- Relatório de métricas a acompanhar (diário, semanal)
