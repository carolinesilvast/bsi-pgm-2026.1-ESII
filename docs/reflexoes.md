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
