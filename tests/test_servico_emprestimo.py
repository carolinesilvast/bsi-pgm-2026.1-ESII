import datetime
import pytest

from models.equipamento import Notebook, Projetor, Cabo


def test_registrar_devolve_true_quando_equipamento_disponivel(servico):

    resultado = servico.registrar(
        1, "Ana", "ana@email.com", 7
    )

    assert resultado is True


def test_registrar_devolve_false_quando_equipamento_indisponivel(
        servico,
        repositorio_fake):

    repositorio_fake.marcar_indisponivel(1)

    resultado = servico.registrar(
        1, "Ana", "ana@email.com", 7
    )

    assert resultado is False


def test_registrar_notifica_usuario_apos_sucesso(
        servico,
        notificador_spy):

    servico.registrar(
        1, "Ana", "ana@email.com", 7
    )

    assert len(notificador_spy.eventos) == 1
    assert notificador_spy.eventos[0][0] == "emprestimo"


@pytest.mark.parametrize(
    "equipamento_id,dias_atraso",
    [
        (1, 2),
        (2, 2),
        (3, 2),
    ]
)
def test_devolver_calcula_multa_correta_para_atraso(
        servico,
        repositorio_fake,
        equipamento_id,
        dias_atraso):

    servico.registrar(
        equipamento_id,
        "Ana",
        "ana@email.com",
        7
    )

    emp = repositorio_fake.buscar_emprestimo(1)

    emp.data_devolucao = (
        datetime.date.today()
        - datetime.timedelta(days=dias_atraso)
    )

    servico.devolver(1)

    assert emp.devolvido is True


def test_devolver_marca_equipamento_como_disponivel(
        servico,
        repositorio_fake):

    servico.registrar(
        1,
        "Ana",
        "ana@email.com",
        7
    )

    servico.devolver(1)

    equipamento = repositorio_fake.buscar_equipamento(1)

    assert equipamento.disponivel is True


def test_devolver_falha_silenciosamente_para_emprestimo_inexistente(
        servico):

    servico.devolver(999)

    assert True
