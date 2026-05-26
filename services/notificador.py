# Notificador: enviar notificações.

class Notificador:

    def notificar_emprestimo(
        self,
        email,
        data_devolucao
    ):
        print(
            f"[EMAIL] {email} — "
            f"empréstimo até {data_devolucao}"
        )

    def notificar_devolucao(
        self,
        email,
        multa
    ):
        print(
            f"[EMAIL] {email} — "
            f"multa R${multa:.2f}"
        )

    def notificar_atraso(
        self,
        email
    ):
        print(
            f"[EMAIL] {email} — "
            f"você está em atraso!"
        )
