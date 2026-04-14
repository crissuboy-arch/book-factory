# Workflow: Pipeline de Construcao de Marca

## Trigger
```
/brand-build empresa="[nome]" categoria="[mercado]" avatar="[descricao]"
```

## Pipeline
```
[Neumeier] Auditoria de brand gap
    ↓
[Neumeier] Mapeamento da categoria + concorrentes (ZAG)
    ↓
[Ogilvy] Pesquisa de percepção do avatar
    ↓
[Neumeier] Task: positioning (declaração de posicionamento)
    ↓
[Ogilvy] Task: brand-identity (personalidade, voz, visual)
    ↓
[Neumeier + Ogilvy] Task: naming (se necessário)
    ↓
OUTPUT:
├── brand-brief.md (documento completo)
├── positioning-statement.md
├── voice-guidelines.md
└── naming-shortlist.md (se solicitado)
```

## Integracao com book-factory
Quando um livro é gerado:
- Define o posicionamento do autor como marca
- Cria a identidade do autor para o livro
- Sugere o nome do método/sistema do livro (se houver)
- Alimenta o copy-master com a voz de marca para toda a copy de lançamento
