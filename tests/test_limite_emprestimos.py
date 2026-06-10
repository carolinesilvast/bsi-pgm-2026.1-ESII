from limite_emprestimos import pode_realizar_emprestimo


def test_usuario_abaixo_do_limite_pode_emprestar():
    assert pode_realizar_emprestimo(
        emprestimos_abertos=2,
        limite=3
    ) is True
