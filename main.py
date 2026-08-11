from app.sistema import SistemaDeEmprestimos


def main():
    sistema = SistemaDeEmprestimos()

    while True:
        print("\n1 - Registrar empréstimo")
        print("2 - Devolver empréstimo")
        print("3 - Listar atrasados")
        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            try:
                equipamento_id = int(input("ID do equipamento: "))
                nome = input("Nome do usuário: ")
                email = input("Email: ")
                dias = int(input("Dias de empréstimo: "))
                sistema.registrar(equipamento_id, nome, email, dias)
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            try:
                emprestimo_id = int(input("ID do empréstimo: "))
                sistema.devolver(emprestimo_id)
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            sistema.listar_atrasados()

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()
