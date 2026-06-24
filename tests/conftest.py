import datetime
import pytest

from models.equipamento import Notebook, Projetor, Cabo
from services.servico_emprestimo import ServicoEmprestimo
from repositories.interfaces import IRepositorioEmprestimo
from services.interfaces import INotificador


# Fake
class RepositorioFake(IRepositorioEmprestimo):

    def __init__(self):
        self._equipamentos = [
            Notebook(1, "Notebook Dell", "notebook"),
            Projetor(2, "Projetor Epson", "projetor"),
            Cabo(3, "Cabo HDMI", "cabo"),
        ]
        self._emprestimos = []

    def buscar_equipamento(self, id):
        return next((e for e in self._equipamentos if e.id == id), None)

    def salvar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def buscar_emprestimo(self, id):
        return next((e for e in self._emprestimos if e.id == id), None)

    def marcar_indisponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = False

    def marcar_disponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = True

    def marcar_devolvido(self, emprestimo_id):
        emp = self.buscar_emprestimo(emprestimo_id)
        if emp:
            emp.devolvido = True

    def listar_em_atraso(self):
        hoje = datetime.date.today()
        return [
            e for e in self._emprestimos
            if not e.devolvido and e.data_devolucao < hoje
        ]

    def proximo_id_emprestimo(self):
        return len(self._emprestimos) + 1


# Spy
class NotificadorSpy(INotificador):

    def __init__(self):
        self.eventos = []

    def notificar_emprestimo(self, email, data_devolucao):
        self.eventos.append(
            ("emprestimo", email, data_devolucao)
        )

    def notificar_devolucao(self, email, multa):
        self.eventos.append(
            ("devolucao", email, multa)
        )

    def notificar_atraso(self, email):
        self.eventos.append(
            ("atraso", email)
        )


@pytest.fixture
def repositorio_fake():
    return RepositorioFake()


@pytest.fixture
def notificador_spy():
    return NotificadorSpy()


@pytest.fixture
def servico(
    repositorio_fake,
    notificador_spy
):
    s = ServicoEmprestimo(
        repositorio_fake
    )

    s.registrar_observer(
        notificador_spy
    )

    return s
