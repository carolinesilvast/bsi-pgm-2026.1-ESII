from datetime import date, timedelta
from models.emprestimo import Emprestimo
from repositories.interfaces import IRepositorioEmprestimo
from services.evento import Evento
from services.observer import Subject


class ServicoEmprestimo(Subject):
    def __init__(self, repositorio: IRepositorioEmprestimo):
        super().__init__()
        self.repositorio = repositorio

    def registrar(self, equipamento_id: int, usuario_nome: str,
                  usuario_email: str, dias: int) -> bool:
        equipamento = self.repositorio.buscar_equipamento(equipamento_id)

        if not equipamento or not equipamento.disponivel:
            return False

        data_emprestimo = date.today()
        data_devolucao = data_emprestimo + timedelta(days=dias)

        emprestimo = Emprestimo(
            id=self.repositorio.proximo_id_emprestimo(),
            equipamento_id=equipamento_id,
            usuario_nome=usuario_nome,
            usuario_email=usuario_email,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao,
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equipamento_id)

        evento = Evento(
            tipo="emprestimo",
            email=usuario_email,
            data=data_devolucao
        )
        self.notificar(evento)

        return True

    def devolver(self, emprestimo_id: int) -> bool:
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)

        if not emprestimo:
            return False

        hoje = date.today()
        atraso = (hoje - emprestimo.data_devolucao).days
        multa = 0.0

        if atraso > 0:
            equipamento = self.repositorio.buscar_equipamento(emprestimo.equipamento_id)
            if equipamento:
                multa = equipamento.calcular_multa(atraso)

        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)
        self.repositorio.marcar_devolvido(emprestimo_id)

        evento = Evento(
            tipo="devolucao",
            email=emprestimo.usuario_email,
            multa=multa
        )
        self.notificar(evento)

        return True

    def listar_atrasados(self) -> list:
        atrasados = self.repositorio.listar_em_atraso()

        for emp in atrasados:
            hoje = date.today()
            dias_atraso = (hoje - emp.data_devolucao).days
            equipamento = self.repositorio.buscar_equipamento(emp.equipamento_id)

            if equipamento:
                multa = equipamento.calcular_multa(dias_atraso)
                print(f"Usuário {emp.usuario_nome}: R${multa:.2f}")

            evento = Evento(
                tipo="atraso",
                email=emp.usuario_email
            )
            self.notificar(evento)

        return atrasados
