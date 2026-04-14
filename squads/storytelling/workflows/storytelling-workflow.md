# Workflow: Pipeline de Desenvolvimento Narrativo

## Descrição
Orquestra os agentes de storytelling para criar a estrutura narrativa completa de qualquer obra.

## Trigger
```
/story-build tipo="[livro/roteiro/curso]" premissa="[ideia]" genero="[genero]" capitulos=[N]
```

## Pipeline

```
FASE 1: CONCEITO
├── [Snyder] Logline em 1 frase
├── [Campbell] Identificação do herói e sua jornada
└── [Harmon] WANT vs NEED do protagonista
      ↓
FASE 2: ESTRUTURA MACRO
├── [Campbell] Mapa dos 12 estágios da Jornada do Herói
├── [Snyder] Beat Sheet completo (15 beats)
└── [Harmon] Story Circle do protagonista
      ↓
FASE 3: PERSONAGENS
├── [Harmon] Ficha psicológica do protagonista
├── [Campbell] Papéis arquetípicos (mentor, guardião, antagonista)
└── [Snyder] Save the Cat moment + Ghost/Falha
      ↓
FASE 4: MAPA DE CAPÍTULOS
├── [Harmon] Sequência de arcos emocionais
├── [Snyder] Verificação de ritmo (nenhum buraco de tensão)
└── [Campbell] Verificação de tema em cada ato
      ↓
OUTPUT FINAL:
├── logline.md
├── story-structure.md (beats + estágios)
├── characters/ (ficha de cada personagem)
├── chapter-map.md (ficha de cada capítulo)
└── theme-tracker.md (como o tema evolui)
```

## Integração com book-factory
Quando ativado pelo pipeline do livro:
- Recebe o manuscrito gerado pelo /book-create
- Analisa e sugere melhorias na estrutura narrativa
- Gera o chapter-map retroativamente para uso no export e marketing
- Alimenta o copy-master com a "história do herói" para a página de vendas
