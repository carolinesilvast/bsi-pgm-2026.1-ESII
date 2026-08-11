import pytest
import datetime
from models.emprestimo import Emprestimo


def test_registrar_devolve_true_quando_equipamento_disponivel(servico):
    resultado = servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    assert resultado is True


def test_registrar_devolve_false_quando_equipamento_indisponivel(servico):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    resultado = servico.registrar(1, "Joao", "joao@ufra.edu.br", 5)
    assert resultado is False


def test_registrar_notifica_usuario_apos_sucesso(servico, notificador_spy):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    assert len(notificador_spy.events) == 1
    assert notificador_spy.events[0].tipo == "emprestimo"
    assert notificador_spy.events[0].email == "ana@ufra.edu.br"


def test_devolver_calcula_multa_correta_para_atraso(servico, repositorio_fake):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    emp = repositorio_fake.buscar_emprestimo(1)
    emp.data_devolucao = datetime.date.today() - datetime.timedelta(days=3)

    servico.devolver(1)
    emprestimo = repositorio_fake.buscar_emprestimo(1)
    assert emprestimo.devolvido is True


def test_devolver_marca_equipamento_como_disponivel(servico, repositorio_fake):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    servico.devolver(1)
    equipamento = repositorio_fake.buscar_equipamento(1)
    assert equipamento.disponivel is True


def test_devolver_falha_silenciosamente_para_emprestimo_inexistente(servico):
    resultado = servico.devolver(999)
    assert resultado is False


def test_registrar_notifica_observer(servico, notificador_spy):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    assert len(notificador_spy.events) == 1
    assert notificador_spy.events[0].tipo == "emprestimo"


def test_devolver_notifica_observer_com_multa(servico, notificador_spy, repositorio_fake):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    emp = repositorio_fake.buscar_emprestimo(1)
    emp.data_devolucao = datetime.date.today() - datetime.timedelta(days=3)
    servico.devolver(1)

    assert len(notificador_spy.events) == 2
    assert notificador_spy.events[1].tipo == "devolucao"
    assert notificador_spy.events[1].email == "ana@ufra.edu.br"


def test_listar_atrasados_notifica_observer(servico, notificador_spy, repositorio_fake):
    servico.registrar(1, "Ana", "ana@ufra.edu.br", 7)
    emp = repositorio_fake.buscar_emprestimo(1)
    emp.data_devolucao = datetime.date.today() - datetime.timedelta(days=3)

    servico.listar_atrasados()

    assert len(notificador_spy.events) == 2
    assert notificador_spy.events[1].tipo == "atraso"
    assert notificador_spy.events[1].email == "ana@ufra.edu.br"
