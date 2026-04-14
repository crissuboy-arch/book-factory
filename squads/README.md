# xQuads — Squads de Especialistas

Sistema modular de agentes de IA especializados que trabalham em conjunto com o book-factory para transformar um manuscrito em um negócio completo de publicação digital.

## Squads Disponíveis

| Squad | Especialidade | Agentes |
|-------|--------------|---------|
| [copy-master](copy-master/) | Copywriting e persuasão | Ogilvy, Kennedy, Halbert, Cialdini, Hormozi, Brunson |
| [storytelling](storytelling/) | Narrativa e estrutura | Campbell, Snyder, Harmon |
| [hormozi-squad](hormozi-squad/) | Ofertas e negócios | Alex Hormozi |
| [brand-squad](brand-squad/) | Marca e posicionamento | Ogilvy, Neumeier |
| [traffic-masters](traffic-masters/) | Tráfego pago e orgânico | Meta, Google, Orgânico |

## Estrutura de Cada Squad

```
squads/[nome-do-squad]/
├── agents/          # Definição de cada agente especialista
├── tasks/           # Templates de tarefas com inputs e outputs
└── workflows/       # Pipelines de orquestração entre agentes
```

## Pipeline Integrado com book-factory

Ao usar `/book-create`, o sistema pode acionar automaticamente:

```
/book-create → manuscrito gerado
      ↓
/book-launch → aciona os squads em sequência:
      ├── storytelling → analisa e valida a estrutura narrativa
      ├── hormozi-squad → cria a oferta e precificação na Hotmart
      ├── brand-squad → posiciona o autor como marca
      ├── copy-master → gera página de vendas + emails + VSL
      └── traffic-masters → cria campanha Meta + Google
```

Ver: [skills/book-launch-pipeline.md](../skills/book-launch-pipeline.md)
