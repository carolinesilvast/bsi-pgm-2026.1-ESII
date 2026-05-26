## Aula 05 — OCP

A hierarquia criada aplicou OCP usando polimorfismo para eliminar os blocos de if/elif do cálculo de multa. Cada tipo de equipamento passou a possuir seu próprio método calcular_multa(), permitindo adicionar novos tipos sem modificar o serviço principal. Isso melhorou a extensibilidade e reduziu o acoplamento entre as regras de negócio e os tipos de equipamento.

Mesmo assim, minha solução possui limites. Se surgir um requisito muito diferente, como cálculo por hora ou baseado no dia da semana, talvez apenas criar subclasses não seja suficiente. A hierarquia pode começar a crescer demais ou concentrar regras muito variadas, dificultando manutenção e entendimento. Nesse caso, provavelmente seria necessário refatorar novamente o projeto, talvez separando a política de multa em estratégias independentes.

Valente comenta no Cap. 5 que o OCP não elimina mudanças futuras, mas busca organizar o sistema para reduzir o impacto das mudanças mais prováveis. Ou seja, o princípio funciona melhor quando conseguimos prever os tipos de variação esperados. Quando aparecem mudanças muito diferentes das previstas originalmente, pode ser necessário reorganizar a arquitetura. Assim, percebi que OCP não significa “nunca modificar”, mas sim estruturar o sistema para evoluir com menos impacto possível nos cenários mais comuns.

---

## Aula 06 - Verificação de LSP

As subclasses Notebook, Projetor e Cabo respeitam o contrato definido pela classe base. O que isso significa, na prática, que calcular_multa(0) retorna 0.0; calcular_multa(-5) também retorna 0.0; a lógica usa max(0, valor), então não surgem multas negativas. Além disso, nenhuma das subclasses lança exceções inesperadas durante o cálculo, mantendo o comportamento esperado pelo ServicoEmprestimo.

Conclusão sobre LSP: está satisfeito. Qualquer subclasse pode substituir Equipamento sem quebrar o funcionamento do serviço.

---

## Aula 06 - DIP

O ServicoEmprestimo deixou de criar suas próprias dependências e passou a trabalhar apenas com as dependências fornecidas externamente. Antes: o serviço controlava diretamente qual repositório e qual notificador eram usados, gerando acoplamento forte. Depois: dependências são fornecidas externamente pelo main.py, reduzindo o acoplamento.Não mandar “nas dependências” e depender apenas de comportamentos esperados facilita substituições de implementação sem mexer no serviço principal.
Apoio conceitual (Valente, Cap. 5): a inversão de dependência reduz o impacto das mudanças, pois módulos de alto nível não dependem de detalhes concretos.
Ao criar versões falsas (fakes) de repositório e notificador para testes, o ServicoEmprestimo continuou funcionando sem acessar dados reais nem enviar emails verdadeiros. Os benefícios reais envolvem a  melhoria da testabilidade do sistema e arquitetura preparada para evoluir com menor impacto entre os módulos.
Conclusão: o DIP foi adotado com sucesso, deixando o sistema mais flexível e mais fácil de manter e testar.
