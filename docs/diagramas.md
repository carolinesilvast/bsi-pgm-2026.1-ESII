# Documento de Design — Sistema de Empréstimos v2.0

**Disciplina:** Engenharia de Software II  
**Aluna:** Caroline Silva Santos  
**Data:** 06/05/2026  


## Decomposição em camadas

A decomposição segue os princípios de **SRP (um motivo para mudar por classe)** e **separação por camadas**, conforme ADR-001.

### Camada models (domínio puro)

| Classe | Motivo para mudar | Por que mora aqui? |
|--------|------------------|----------------------|
| `Equipamento` | Alteração nos atributos de um equipamento (nome, tipo, disponibilidade) | Representa um conceito do domínio, sem regras de negócio ou persistência. Alta coesão. |
| `Emprestimo` | Alteração nos dados de um empréstimo (datas, status, multa) | Mesmo princípio: apenas estrutura de dados do domínio. Isola o que o negócio entende por "empréstimo". |

---

### Camada services (lógica de aplicação)

| Classe | Motivo para mudar | Por que mora aqui? |
|--------|------------------|----------------------|
| `ServicoEmprestimo` | Regras de negócio de empréstimo (cálculo de multa, validação de disponibilidade, etc.) | Coordena os casos de uso. Aplica SRP: só contém lógica de negócio, sem interface ou persistência. |
| `Notificador` | Troca de canal de notificação (ex.: e-mail → SMS) ou template de mensagem | Responsabilidade única: enviar mensagens. Mudanças externas (provedor de e-mail, formato) ficam aqui. |

---

### Camada repositories (acesso a dados)

| Classe | Motivo para mudar | Por que mora aqui? |
|--------|------------------|----------------------|
| `RepositorioEquipamento` | Troca de fonte de dados (lista → banco → API) | Esconde a estrutura de dados interna. Cliente chama `buscar_por_id()` sem saber se é dict, SQL, etc. |
| `RepositorioEmprestimo` | Troca de persistência ou mudança no esquema de armazenamento | Mesmo princípio de ocultamento. Listas internas são privadas (`_emprestimos`). |

---

### Camada interface (interação com usuário)

| Classe | Motivo para mudar | Por que mora aqui? |
|--------|------------------|----------------------|
| `CLI` | Alteração no formato do menu, mensagens, ou fluxo de entrada/saída | Isola completamente a apresentação. A classe `Sistema` original violava SRP ao misturar menu com regras de negócio. |

---

### Inicialização

| Arquivo | Motivo para mudar | Por que mora aqui? |
|---------|------------------|----------------------|
| `main.py` | Mudança na forma de instanciar dependências (ex.: injeção de dependência) | Única responsabilidade: montar o sistema e iniciar. Nenhuma lógica de domínio. |

---

## Diagramas de sequência

### UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram
    actor Atendente
    participant CLI as InterfaceCLI
    participant Servico as ServicoEmprestimo
    participant RepoEquip as RepositorioEquipamento
    participant RepoEmp as RepositorioEmprestimo
    participant Notif as Notificador
    participant Equip as Equipamento

    Atendente->>CLI: informa id, nome, email, dias
    CLI->>Servico: registrar_emprestimo(id, nome, email, dias)

    Servico->>RepoEquip: buscar_por_id(id)
    RepoEquip->>Equip: cria Equipamento
    Equip-->>RepoEquip: equipamento
    RepoEquip-->>Servico: equipamento

    alt equipamento invalido ou indisponivel
        Servico-->>CLI: erro
        CLI-->>Atendente: Equipamento nao disponivel
    else disponivel
        Servico->>Servico: calcular_data_devolucao(dias)
        Servico->>RepoEmp: criar_emprestimo(dados)
        RepoEmp-->>Servico: emprestimo_criado

        Servico->>RepoEquip: marcar_indisponivel(id)

        Servico->>Notif: enviar_notificacao_emprestimo(email, data)
        Notif-->>Servico: notificado

        Servico-->>CLI: sucesso
        CLI-->>Atendente: Emprestimo registrado com sucesso
    end
```

### UC02 — Registrar Devolução

```mermaid
sequenceDiagram
    actor Atendente
    participant CLI as InterfaceCLI
    participant Servico as ServicoEmprestimo
    participant RepoEmp as RepositorioEmprestimo
    participant RepoEquip as RepositorioEquipamento
    participant Notif as Notificador
    participant Emprestimo as Emprestimo

    Atendente->>CLI: informa id_emprestimo
    CLI->>Servico: registrar_devolucao(id_emprestimo)

    Servico->>RepoEmp: buscar_por_id(id_emprestimo)
    RepoEmp-->>Servico: emprestimo

    alt emprestimo invalido ou ja devolvido
        Servico-->>CLI: erro
        CLI-->>Atendente: Emprestimo invalido ou ja devolvido
    else valido
        Servico->>Emprestimo: calcular_atraso()
        Emprestimo-->>Servico: dias_atraso

        Servico->>Servico: calcular_multa(tipo, dias_atraso)
        Note over Servico: Multa por tipo: Notebook R$10/dia, Projetor R$15/dia, Cabo R$2/dia

        Servico->>RepoEmp: marcar_como_devolvido(id, multa)
        Servico->>RepoEquip: liberar_equipamento(equipamento_id)

        Servico->>Notif: enviar_notificacao_multa(email, multa)
        Notif-->>Servico: notificado

        Servico-->>CLI: sucesso com multa
        CLI-->>Atendente: Devolucao registrada. Multa: R$ X
    end
```

### UC03 — Listar Empréstimos em Atraso

```mermaid
sequenceDiagram
    actor Atendente
    participant CLI as InterfaceCLI
    participant Servico as ServicoEmprestimo
    participant RepoEmp as RepositorioEmprestimo
    participant Notif as Notificador

    Atendente->>CLI: solicita lista de atrasados
    CLI->>Servico: listar_atrasados()

    Servico->>RepoEmp: buscar_atrasados_nao_devolvidos()
    RepoEmp-->>Servico: lista_emprestimos

    loop para cada emprestimo em atraso
        Servico->>Servico: calcular_atraso()
        Servico->>Servico: calcular_multa()
        Servico->>Notif: enviar_notificacao_atraso(email, dias, multa)
        Notif-->>Servico: notificado
    end

    Servico-->>CLI: lista_formatada
    CLI-->>Atendente: exibe nome, dias atraso, multa
```
