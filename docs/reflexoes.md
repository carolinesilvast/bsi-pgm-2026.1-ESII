## Aula 05 — OCP

A hierarquia criada aplicou OCP usando polimorfismo para eliminar os blocos de if/elif do cálculo de multa. Cada tipo de equipamento passou a possuir seu próprio método calcular_multa(), permitindo adicionar novos tipos sem modificar o serviço principal. Isso melhorou a extensibilidade e reduziu o acoplamento entre as regras de negócio e os tipos de equipamento.

Mesmo assim, minha solução possui limites. Se surgir um requisito muito diferente, como cálculo por hora ou baseado no dia da semana, talvez apenas criar subclasses não seja suficiente. A hierarquia pode começar a crescer demais ou concentrar regras muito variadas, dificultando manutenção e entendimento. Nesse caso, provavelmente seria necessário refatorar novamente o projeto, talvez separando a política de multa em estratégias independentes.

Valente comenta no Cap. 5 que o OCP não elimina mudanças futuras, mas busca organizar o sistema para reduzir o impacto das mudanças mais prováveis. Ou seja, o princípio funciona melhor quando conseguimos prever os tipos de variação esperados. Quando aparecem mudanças muito diferentes das previstas originalmente, pode ser necessário reorganizar a arquitetura. Assim, percebi que OCP não significa “nunca modificar”, mas sim estruturar o sistema para evoluir com menos impacto possível nos cenários mais comuns.
