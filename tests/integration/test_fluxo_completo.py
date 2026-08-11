from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador_email import NotificadorEmail
from services.servico_emprestimo import ServicoEmprestimo


def test_fluxo_registrar_devolver_com_componentes_reais():
    # Arrange - componentes REAIS
    repository = RepositorioEmprestimo()
    servico = ServicoEmprestimo(repository)
    servico.registrar_observer(NotificadorEmail())

    # Act
    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)

    # Assert
    assert sucesso is True
    emprestimo = repository.buscar_emprestimo(1)
    assert emprestimo is not None
    assert emprestimo.equipamento_id == 1
    assert repository.buscar_equipamento(1).disponivel is False
