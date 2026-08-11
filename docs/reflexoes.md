## Aula 09 — TDD

Comparando TDD e BDD, considero que o BDD comunica melhor com um cliente não técnico. 
Os cenários escritos no formato Dado–Quando–Então utilizam uma linguagem próxima das 
regras de negócio, permitindo que clientes, analistas e desenvolvedores entendam o 
comportamento esperado do sistema sem precisar conhecer programação. Já o TDD é mais 
adequado para a equipe de desenvolvimento, pois os testes automatizados verificam o 
funcionamento do código de forma precisa e ajudam a evitar erros durante alterações futuras.

Eu utilizaria BDD nas etapas de levantamento e validação de requisitos, quando é importante
alinhar expectativas com usuários e clientes. Por outro lado, utilizaria TDD durante a 
implementação das funcionalidades, garantindo qualidade, segurança para refatorações e
maior confiabilidade na evolução do sistema.

## Aula 10 — Factory e Facade

A Factory centraliza a criação dos objetos em um único local. Embora ela utilize um if/elif 
ou um mapa para decidir qual classe instanciar, esse acoplamento fica concentrado apenas na 
fábrica. Isso é aceitável porque evita que a mesma lógica de decisão fique espalhada por várias 
partes do sistema. Dessa forma, se um novo tipo de equipamento for adicionado, a alteração 
ocorre principalmente na fábrica, enquanto o restante do sistema continua desacoplado das
classes concretas. Assim, a fábrica "paga" o custo desse acoplamento para manter as demais
classes mais aderentes ao princípio Open/Closed (OCP). Conforme discutido por Valente no 
Capítulo 6, a Factory é útil para encapsular a criação de objetos e reduzir dependências diretas.

A introdução da Facade não desfaz o DIP aplicado anteriormente. A classe SistemaDeEmprestimos 
atua como uma raiz de composição, responsável apenas por montar os objetos concretos utilizados 
na execução da aplicação. As regras de negócio continuam no ServicoEmprestimo, que ainda depende 
de abstrações e permite a injeção de dependências. Isso pode ser observado nos testes, que
continuam utilizando dublês, como repositórios falsos e spies, diretamente no serviço. 
Portanto, a Facade apenas simplifica o ponto de entrada da aplicação, sem alterar a arquitetura 
baseada em DIP nem comprometer a testabilidade do sistema.

## Aula 11 — Strategy e Observer

Na Aula 11, a principal mudança foi a substituição de soluções baseadas em herança e acoplamento 
direto por composição e desacoplamento de comportamento. No caso do Strategy, o cálculo de multa 
que antes estava distribuído entre subclasses de Equipamento (Notebook, Projetor e Cabo) foi extraído
para uma hierarquia de estratégias. Isso permitiu que o Equipamento deixasse de definir regras de 
negócio e passasse apenas a delegar o cálculo para um objeto especializado. Essa evolução mostra 
que a composição é mais flexível que a herança por tipo, pois permite trocar algoritmos em tempo 
de execução sem alterar a estrutura da classe. Assim, o Open/Closed Principle é mantido de forma 
mais eficiente, já que novas regras de multa podem ser adicionadas sem modificar o Context.

No Observer, o Serviço de Empréstimo deixou de depender diretamente de um notificador concreto e 
passou a emitir eventos para múltiplos observadores. Isso melhora o SRP, pois o serviço não precisa 
mais saber como cada notificação é enviada, e também reforça o OCP, já que novos observadores podem 
ser adicionados sem modificar o serviço. O DIP também é respeitado, pois o módulo de alto nível 
depende de abstrações (Observer), não de implementações concretas.

## Aula 12 - Refactoring e Code Smells

### Rede de segurança

O pytest serviu como rede de segurança durante toda a atividade. A cada passo, executar a suíte e vê-la verde autorizava a continuidade. Quando um teste falhou, o passo era desfeito e revista.

Refatorar com testes é seguro: cada mudança é verificada imediatamente. Refatorar sem testes é perigoso: o comportamento pode quebrar silenciosamente. A definição de refactoring exige preservação do comportamento observável - e isso só é verificável com testes.

### Falso positivo - subclasses esvaziadas

As subclasses vazias (Notebook, Projetor, Cabo) aparentam Data Class mas são intencionais: são marcadores de tipo. Aplicar Inline Class desfaria o Strategy e reverteria o OCP obtido. É um falso positivo bem reconhecido.

## Aula 13 - CI/CD e Production Readiness

### Pipeline de CI

A pipeline (lint + testes + cobertura ≥ 80%) automatiza a verificação de qualidade a cada push. O commit de quebra proposital e sua correção demonstram o valor do CI: feedback rápido e rastreável.

### Síntese executiva

Ver production_readiness.md para a análise completa.

O uso de eventos como dict foi uma decisão consciente para simplificar a implementação inicial, 
mas representa um smell (Primitive Obsession), pois falta tipagem e estrutura formal. 
Segundo Valente (Cap. 6), essa simplificação é aceitável em fases iniciais, desde que seja refatorada
posteriormente.
