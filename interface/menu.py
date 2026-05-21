# Menu: realizar interação com o usuário.

from services.servico_emprestimo import ServicoEmprestimo


class Menu:

    def __init__(self):
        self.servico = ServicoEmprestimo()

    def executar(self):
        while True:
            print("\n1-Registrar  2-Devolver  3-Atrasados  0-Sair")

            op = input("Opção: ")

            if op == "1":
                self.servico.registrar(
                    int(input("ID equipamento: ")),
                    input("Nome: "),
                    input("Email: "),
                    int(input("Dias: "))
                )

            elif op == "2":
                self.servico.devolver(
                    int(input("ID empréstimo: "))
                )

            elif op == "3":
                self.servico.listar_atrasados()

            elif op == "0":
                break
