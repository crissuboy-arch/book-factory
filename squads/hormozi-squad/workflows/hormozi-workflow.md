# Workflow: Pipeline de Negocio Hormozi

## Trigger
```
/hormozi-build produto="[nome]" avatar="[descricao]" preco_desejado="R$[X]"
```

## Pipeline
```
[Hormozi] Define Dream Outcome
    ↓
[Hormozi] Mapeia obstáculos do avatar
    ↓
[Hormozi] Task: irresistible-offer (Grand Slam Offer)
    ↓
[Hormozi] Task: pricing (ladder de preços)
    ↓
[Hormozi] Task: sales-funnel (estrutura completa)
    ↓
→ Alimenta copy-master com a oferta estruturada
→ Alimenta traffic-masters com LTV calculado (define budget de anúncios)
→ Alimenta book-factory com a oferta do livro na Hotmart
```

## Integracao com book-factory
Quando um livro é gerado:
- Define automaticamente o preço baseado no ROI do leitor
- Estrutura a oferta completa (livro + bônus digitais)
- Projeta o funil: livro gratuito/baixo custo → curso → mentoria
- Calcula o LTV do autor-empreendedor
