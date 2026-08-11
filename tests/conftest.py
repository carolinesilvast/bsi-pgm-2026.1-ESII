import pytest
from datetime import date, timedelta
from models.equipamento import Notebook, Projetor, Cabo
from models.emprestimo import Emprestimo
from models.multa_strategy import MultaPorDia
from models.fabrica_equipamento import FabricaEquipamento
from repositories.interfaces import IRepositorioEmprestimo
from services.evento import Evento
from services.interfaces import INotificador
from services.observer import Observer
from services.servico_emprestimo import ServicoEmprestimo


class RepositorioFake(IRepositorioEmprestimo):
    def __init__(self):
        criar = FabricaEquipamento.criar
        self._equipamentos = [
            criar("notebook", 1, "Notebook Dell"),
            criar("projetor", 2, "Projetor Epson"),
            criar("cabo", 3, "Cabo HDMI"),
        ]
        self._emprestimos = []

    def buscar_equipamento(self, id: int):
        for e in self._equipamentos:
            if e.id == id:
                return e
        return None

    def salvar_emprestimo(self, emprestimo: Emprestimo) -> None:
        self._emprestimos.append(emprestimo)

    def buscar_emprestimo(self, id: int):
        for e in self._emprestimos:
            if e.id == id:
                return e
        return None

    def marcar_indisponivel(self, equip_id: int) -> None:
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = False

    def marcar_disponivel(self, equip_id: int) -> None:
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = True

    def marcar_devolvido(self, emprestimo_id: int) -> None:
        emp = self.buscar_emprestimo(emprestimo_id)
        if emp:
            emp.devolvido = True

    def listar_em_atraso(self) -> list:
        hoje = date.today()
        return [e for e in self._emprestimos if not e.devolvido and e.data_devolucao < hoje]

    def proximo_id_emprestimo(self) -> int:
        return len(self._emprestimos) + 1


class NotificadorSpy(Observer):
    def __init__(self):
        self.events = []

    def update(self, evento: Evento) -> None:
        self.events.append(evento)


class NotificadorMock(INotificador):
    def __init__(self):
        self.events = []

    def notificar_emprestimo(self, email, data_devolucao):
        self.events.append(("emprestimo", email, data_devolucao))

    def notificar_devolucao(self, email, multa):
        self.events.append(("devolucao", email, multa))

    def notificar_atraso(self, email):
        self.events.append(("atraso", email))


@pytest.fixture
def repositorio_fake():
    return RepositorioFake()


@pytest.fixture
def notificador_spy():
    return NotificadorSpy()


@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    s = ServicoEmprestimo(repositorio_fake)
    s.registrar_observer(notificador_spy)
    return s
