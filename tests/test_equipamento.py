import pytest

from models.equipamento import Notebook, Projetor, Cabo


@pytest.mark.parametrize(
    "equipamento,dias,multa_esperada",
    [
        (Notebook(1, "Dell", "notebook"), 2, 20.0),
        (Notebook(1, "Dell", "notebook"), 3, 30.0),

        (Projetor(2, "Epson", "projetor"), 2, 30.0),
        (Projetor(2, "Epson", "projetor"), 3, 45.0),

        (Cabo(3, "HDMI", "cabo"), 2, 4.0),
        (Cabo(3, "HDMI", "cabo"), 3, 6.0),
    ]
)
def test_calcular_multa_atraso_positivo(
        equipamento,
        dias,
        multa_esperada):

    assert (
        equipamento.calcular_multa(dias)
        == multa_esperada
    )


@pytest.mark.parametrize(
    "equipamento",
    [
        Notebook(1, "Dell", "notebook"),
        Projetor(2, "Epson", "projetor"),
        Cabo(3, "HDMI", "cabo"),
    ]
)
def test_calcular_multa_atraso_negativo_retorna_zero(
        equipamento):

    assert (
        equipamento.calcular_multa(-5)
        == 0.0
    )
