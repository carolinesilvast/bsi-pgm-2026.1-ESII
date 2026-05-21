# Problemas Identificados — Leitura Inicial do Código

1. A lógica de cálculo de multa aparece repetida em mais de um lugar. Se precisar mudar a regra, será necessário alterar em vários pontos;
2. O “envio de email”  aparece em três lugares diferentes. Além de repetido, está misturado com a lógica principal, o que dificulta manutenção;
3. Não existe nenhuma forma de testar os métodos sem executar o sistema completo;
4. A classe faz muitas coisas ao mesmo tempo: busca dados, calcula multa, altera estado, envia notificação. Isso deixa o código confuso;
5. Se for criado um novo tipo, será necessário alterar o código em vários lugares.

---

## Minha leitura inicial

*(Espaço reservado para o estudante preencher)*

Exemplo de entradas:
- "A classe faz muita coisa ao mesmo tempo"
- "Tem código de e-mail misturado com o cálculo de multa"
- "O mesmo cálculo aparece duas vezes no código"
- "As listas de equipamentos estão fora da classe, soltas no arquivo"

---

## Revisão com vocabulário técnico

| Linguagem livre (Aula 1)                                            | Vocabulário técnico (hoje)                                                                                           |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| "O mesmo cálculo aparece duas vezes no código"                      | Violação de DRY: cálculo de multa duplicado em mais de um método                                                     |
| "Tem código de e-mail misturado com o cálculo de multa"             | Responsabilidades misturadas: notificação e regra de negócio no mesmo método — viola SRP                             |
| "A classe faz muita coisa ao mesmo tempo"                           | Sistema tem baixa coesão: acesso a dados, cálculo de multa, alteração de estado e notificação misturados — viola SRP |
| "As listas de equipamentos estão fora da classe, soltas no arquivo" | Acoplamento por variável global: Sistema depende de estado compartilhado                                             |
