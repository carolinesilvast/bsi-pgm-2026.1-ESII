# ServicoEmprestimo: executar regras de negócio.

import datetime

from models.emprestimo import Emprestimo


class ServicoEmprestimo:

    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):

        equipamento = self.repositorio.buscar_equipamento(
            equipamento_id
        )

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

        self.notificador.notificar_emprestimo(
            usuario_email,
            data_devolucao
        )

        return True

    def devolver(self, emprestimo_id):

        emprestimo = self.repositorio.buscar_emprestimo(
            emprestimo_id
        )

        if emprestimo is None or emprestimo.devolvido:
            print("Empréstimo inválido ou já devolvido")
            return

        emprestimo.devolvido = True

        hoje = datetime.date.today()

        atraso = (
            hoje - emprestimo.data_devolucao
        ).days

        equipamento = self.repositorio.buscar_equipamento(
            emprestimo.equipamento_id
        )

        multa = equipamento.calcular_multa(atraso)

        if equipamento:
            equipamento.disponivel = True

        self.notificador.notificar_devolucao(
            emprestimo.usuario_email,
            multa
        )

        print(f"Devolução registrada. Multa: R${multa:.2f}")

    def listar_atrasados(self):

        hoje = datetime.date.today()

        for e in self.repositorio.listar_emprestimos():

            if not e.devolvido and e.data_devolucao < hoje:

                atraso = (
                    hoje - e.data_devolucao
                ).days

                equipamento = self.repositorio.buscar_equipamento(
                    e.equipamento_id
                )

                multa = equipamento.calcular_multa(atraso)

                print(
                    f"{e.usuario_nome} — "
                    f"{atraso} dias — "
                    f"R${multa:.2f}"
                )

                self.notificador.notificar_atraso(
                    e.usuario_email
                )
