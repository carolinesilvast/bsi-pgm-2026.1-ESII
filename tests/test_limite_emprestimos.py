from limite_emprestimos import pode_realizar_emprestimo


def test_usuario_abaixo_do_limite_pode_emprestar():
    assert pode_realizar_emprestimo(
        emprestimos_abertos=2,
        limite=3
    ) is True

def test_usuario_no_limite_nao_pode_emprestar():
    assert pode_realizar_emprestimo(
        emprestimos_abertos=3,
        limite=3
    ) is False
