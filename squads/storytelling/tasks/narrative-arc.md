# Task: Arco Narrativo

## Objetivo
Mapear o arco narrativo completo de uma obra — a progressão de tensão, emoção e tema do início ao fim — garantindo que cada capítulo/cena tem propósito dramático claro.

## Inputs Necessários
```
obra: [título e tipo]
numero_capitulos: [quantidade]
estrutura_base: [Jornada do Herói / Beat Sheet / Story Circle / híbrido]
tema_central: [a verdade que a história comunica]
pergunta_dramatica: [a pergunta que a audiência quer ver respondida]
tom: [dramático / cômico / suspense / épico / íntimo]
```

## Ferramentas por Fase

### MAPEAMENTO MACRO — Curva de Tensão
```
Tensão
  │                                    ★ CLÍMAX
  │                              ╱╲
  │                         ╱       ╲
  │              Midpoint ╱           ╲ Resolução
  │            ╱        ╲╱
  │     ╱ Catalyst
  │ ╱
  └──────────────────────────────── Tempo/Capítulos
  Setup    2B    Ato 2B   All Is Lost  Finale
```

### MAPEAMENTO POR CAPÍTULO
Para cada capítulo, definir:
```
Capítulo [N]: [Título]
- Posição na estrutura: [qual beat do Snyder / qual estágio de Campbell]
- Objetivo dramático: [o que muda neste capítulo]
- Tensão de entrada: [nível 1-10]
- Tensão de saída: [nível 1-10]
- Revelação ou virada: [o que o leitor descobre]
- Linha emocional do herói: [o que sente]
- Linha do tema: [como este capítulo reforça o tema]
- Gancho de saída: [o que faz o leitor precisar ir para o próximo]
```

### VERIFICAÇÃO DE RITMO (Harmon)
Garantir que a sequência emocional varia:
- Não ter 3 capítulos de alta tensão seguidos sem respiração
- Não ter 2 capítulos de alívio seguidos antes de um grande momento
- Cada cena de alívio cônico deve ter subtexto dramático

### VERIFICAÇÃO DE TEMA (Campbell)
Cada ato deve reforçar o tema central de forma diferente:
- **Ato 1**: O herói vive a AUSÊNCIA do tema (não sabe a verdade)
- **Ato 2A**: O tema é sugerido por aliados/eventos (começa a questionar)
- **Ato 2B**: O herói resiste ativamente ao tema (a crise)
- **Ato 3**: O herói ABRAÇA o tema (a transformação)

## Template de Capítulo

```markdown
## Capítulo [N] — [TÍTULO]

**Beat (Snyder)**: [nome do beat]
**Estágio Campbell**: [nome do estágio]
**Story Circle (Harmon)**: [passo 1-8]

### O que acontece (eventos externos)
[2-3 frases descrevendo os eventos principais]

### O que muda (eventos internos)
[Como o herói pensa/sente diferente no final vs. início do capítulo]

### Revelação para o leitor
[O que o leitor descobre que o herói ainda não sabe, ou vice-versa]

### Gancho final
[A frase, cena ou pergunta que garante que o leitor vira a página]

### Conexão temática
[Como este capítulo avança o tema central]
```

## Output Esperado
- Mapa visual da curva de tensão (texto/ASCII)
- Ficha de cada capítulo no template acima
- Lista de revelações ordenadas por capítulo
- Verificação de ritmo: nenhum "buraco emocional" ou "pico sem base"
- Checklist de tema: cada um dos 4 atos reforça o tema de forma diferente
