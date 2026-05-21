# ServicoEmprestimo: executar regras de negócio.

import datetime

from models.emprestimo import Emprestimo
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador


class ServicoEmprestimo:

    def __init__(self):
        self.repositorio = RepositorioEmprestimo()
        self.notificador = Notificador()

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        equipamento = self.repositorio.buscar_equipamento(equipamento_id)

        if equipamento is None or not equipamento.disponivel:
            print("Equipamento inválido ou indisponível")
            return False

        data_emprestimo = datetime.date.today()
        data_devolucao = data_emprestimo + datetime.timedelta(days=dias)

        emprestimo = Emprestimo(
            id=len(self.repositorio.emprestimos) + 1,
            equipamento_id=equipamento.id,
            equipamento_nome=equipamento.nome,
            tipo=equipamento.tipo,
            usuario_nome=usuario_nome,
            usuario_email=usuario_email,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        equipamento.disponivel = False

        self.notificador.enviar(
            usuario_email,
            f"empréstimo até {data_devolucao}"
        )

        return True

    def devolver(self, emprestimo_id):
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)

        if emprestimo is None or emprestimo.devolvido:
            print("Empréstimo inválido ou já devolvido")
            return

        emprestimo.devolvido = True

        hoje = datetime.date.today()
        atraso = (hoje - emprestimo.data_devolucao).days

        equipamento = self.repositorio.buscar_equipamento(
            emprestimo.equipamento_id
        )

        multa = equipamento.calcular_multa(atraso)

        if equipamento:
            equipamento.disponivel = True

        self.notificador.enviar(
            emprestimo.usuario_email,
            f"multa R${multa:.2f}"
        )

        print(f"Devolução registrada. Multa: R${multa:.2f}")

    def listar_atrasados(self):
        hoje = datetime.date.today()

        for e in self.repositorio.listar_emprestimos():
            if not e.devolvido and e.data_devolucao < hoje:

                atraso = (hoje - e.data_devolucao).days

                equipamento = self.repositorio.buscar_equipamento(
                    e.equipamento_id
                )

                multa = equipamento.calcular_multa(atraso)

                print(f"{e.usuario_nome} — {atraso} dias — R${multa:.2f}")

                self.notificador.enviar(
                    e.usuario_email,
                    "você está em atraso!"
                )
