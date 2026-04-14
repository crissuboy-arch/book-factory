# Workflow: Pipeline de Trafego para Lancamento

## Trigger
```
/traffic-launch produto="[nome]" preco="R$[X]" budget="R$[X]" data_lancamento="[DD/MM]"
```

## Pipeline

```
[Estrategista] Task: ads-strategy
  → Define canal principal, budget por canal, cronograma
      ↓
PARALELO:
├── [Meta Specialist] Task: meta-ads-campaign
│     → Estrutura, copy e briefing de criativos Meta
│
└── [Google Specialist] Task: google-ads-campaign
      → Search keywords, RSAs e YouTube roteiro
          ↓
[Orgânico] Calendário de conteúdo orgânico (suporte ao pago)
          ↓
OUTPUT:
├── traffic-strategy.md (estratégia geral)
├── meta-campaign.md (estrutura + copy)
├── google-campaign.md (estrutura + keywords + RSAs)
├── creative-briefs/ (briefings para designer/editor)
│     ├── video-brief.md
│     ├── image-brief.md
│     └── carousel-brief.md
└── content-calendar.md (orgânico de apoio)
```

## Cronograma de Lancamento

```
D-30: Instalar pixel/tag + configurar conversões
D-21: Criar audiências de remarketing (começar a popular)
D-14: Lançar campanha de Awareness (YouTube + Meta)
D-7:  Aumentar frequência + adicionar retargeting
D-3:  Aumentar budget 50% + ativar urgência nos anúncios
D-Day: Monitorar a cada 2h + ajustar lances se necessário
D+7:  Analisar resultados + relatório de performance
```

## Integracao com book-factory
Quando um livro é gerado:
1. Extrai título, subtítulo e sinopse para usar em anúncios
2. Usa as descrições de imagens dos capítulos como briefing de criativos
3. Alimenta os anúncios com o avatar definido pelo book-factory
4. Conecta com copy-master para garantir consistência de mensagem entre anúncio e landing page
