def atingiu_limite(
    emprestimos_abertos,
    limite
):
    return emprestimos_abertos >= limite


def pode_realizar_emprestimo(
    emprestimos_abertos,
    limite
):
    return not atingiu_limite(
        emprestimos_abertos,
        limite
    )
