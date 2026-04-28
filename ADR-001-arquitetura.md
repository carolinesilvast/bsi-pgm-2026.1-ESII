# ADR-001 — Arquitetura do Sistema

## Contexto
O sistema precisa atender aos requisitos:
- RNF03: permitir adicionar novos tipos sem alterar vários módulos
- RNF04: permitir testes isolados sem depender de entrada do usuário

O código atual não atende isso, pois mistura tudo em um único arquivo.

## Opções consideradas

- Arquivo único:
  Simples, porém difícil de manter e testar.

- MVC:
  Muito complexo para um sistema simples de linha de comando.

- Em camadas:
  Separa responsabilidades e facilita manutenção e testes.

## Decisão

Foi escolhida a arquitetura em camadas, com:

- models → dados (equipamentos, empréstimos)
- services → regras de negócio
- repository → acesso aos dados
- interface → interação com o usuário (menu)
- main.py → ponto de entrada

## Consequências

- Código mais organizado
- Facilita testes
- Facilita manutenção
- Um pouco mais complexo inicialmente
