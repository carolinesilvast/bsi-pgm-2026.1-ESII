# Diagnóstico de Code Smells - Aula 12

| # | Arquivo:linha | Smell (nome técnico) | Refactoring proposto | Justificativa |
|---|---------------|----------------------|---------------------|---------------|
| 1 | services/servico_emprestimo.py:45 | Mysterious Name | Rename | A variável `d` não revela que representa dias de empréstimo |
| 2 | services/servico_emprestimo.py:78 | Long Method | Extract Function | O método `listar_atrasados` reúne iteração, cálculo e notificação |
| 3 | services/notificador_email.py:12 | Primitive Obsession | Replace Primitive with Object | O evento como dict foi substituído por @dataclass Evento |
| 4 | models/equipamento.py:12 | Mysterious Name | Rename | O campo `tipo` poderia ser mais descritivo |
| 5 | models/fabrica_equipamento.py:8 | Duplicated Code | Extract Function | A criação de equipamentos repete a mesma estrutura |
| 6 | models/equipamento.py:20-22 | Smell aparente - não refatorado | Inline Class (não aplicado) | As subclasses Notebook, Projetor e Cabo ficaram vazias após o Strategy. São mantidas como rótulos de tipo por design, pois representam tipos de equipamento e desfazer isso reverteria o OCP obtido na Aula 11. |

## Falso positivo identificado

As subclasses esvaziadas após a aplicação do Strategy (Notebook, Projetor, Cabo) aparentam ser Data Classes vazias. Porém, são mantidas intencionalmente como marcadores de tipo, pois:

1. O sistema precisa distinguir entre tipos de equipamento
2. Inline Class desfaria o Strategy e o OCP obtidos
3. A decisão de usar composição (Strategy) em vez de herança é o padrão correto
