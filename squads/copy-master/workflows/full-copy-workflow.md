# Workflow: Pipeline Completo de Copy para Lançamento

## Descrição
Orquestra todos os agentes e tasks do copy-master para gerar o pacote completo de copy de um lançamento de produto digital em sequência lógica.

## Trigger
```
/copy-launch produto="[nome]" avatar="[descrição]" resultado="[transformação]" preco="[R$X]"
```

## Pipeline de Execução

```
FASE 1: FUNDAÇÃO (Definição Estratégica)
│
├── [Ogilvy] Pesquisa do produto e avatar
│     └── Output: Documento de posicionamento
│
├── [Hormozi] Estrutura da oferta e value stack
│     └── Output: Oferta completa com preços
│
└── [Cialdini] Mapeamento de gatilhos e objeções
      └── Output: Mapa de influência

         ↓

FASE 2: COPY PRINCIPAL
│
├── [Halbert + Ogilvy] Task: headlines (20+ opções)
│     └── Output: Top 5 headlines testáveis
│
├── [Kennedy + Brunson] Task: sales-letter ou sales-page
│     └── Output: Copy principal completa
│
└── [Halbert] Task: bullets (30+ bullets)
      └── Output: Top 10 bullets para página

         ↓

FASE 3: FUNIL E SEQUÊNCIA
│
├── [Brunson] Task: vsl-script
│     └── Output: Script VSL completo
│
└── [Kennedy + Brunson] Task: launch-email (7 emails)
      └── Output: Sequência completa de lançamento

         ↓

FASE 4: REVISÃO E OTIMIZAÇÃO
│
├── [Cialdini] Auditoria de gatilhos mentais em toda copy
├── [Ogilvy] Checagem de especificidade e fatos
└── [Kennedy] Checagem de clareza de CTA e urgência

         ↓

OUTPUT FINAL:
├── sales-page.md (página de vendas completa)
├── vsl-script.md (script do vídeo)
├── email-sequence/ (7 emails)
├── headlines.md (top 5 testáveis)
├── bullets.md (top 10)
└── copy-brief.md (resumo estratégico)
```

## Regras de Colaboração entre Agentes
- Ogilvy sempre revisa especificidade — nenhuma afirmação vaga passa
- Kennedy sempre verifica se cada peça tem um CTA claro
- Cialdini valida que os 7 princípios estão presentes
- Hormozi garante que a oferta é o centro de tudo
- Halbert é o "leitor final" — se ele trovar lendo em voz alta, reescreve
- Brunson verifica se a "nova oportunidade" está clara (não é "jeito melhor")

## Critérios de Qualidade
- [ ] Headline passa no teste de Halbert: você pararia para ler às 3h da manhã?
- [ ] Oferta passa no teste de Hormozi: o cliente se sente idiota em recusar?
- [ ] Copy passa no teste de Ogilvy: cada afirmação é específica e verificável?
- [ ] Sequência de email tem ritmo de Kennedy: cada email puxa para o próximo?
- [ ] VSL tem hook de Halbert: os primeiros 10 segundos são impossíveis de ignorar?
- [ ] Todos os 7 gatilhos de Cialdini estão presentes em algum ponto do funil?
