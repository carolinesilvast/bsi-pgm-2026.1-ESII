# main: iniciar o sistema.

from interface.menu import Menu

from repositories.repositorio_emprestimo import (
    RepositorioEmprestimo
)

from services.notificador import Notificador

from services.servico_emprestimo import (
    ServicoEmprestimo
)


def main():

    repositorio = RepositorioEmprestimo()

    notificador = Notificador()

    servico = ServicoEmprestimo(
        repositorio,
        notificador
    )

    menu = Menu(servico)

    menu.executar()


if __name__ == "__main__":
    main()
