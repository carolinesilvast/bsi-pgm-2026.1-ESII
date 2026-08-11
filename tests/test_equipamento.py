import pytest
from models.equipamento import Notebook, Projetor, Cabo
from models.multa_strategy import MultaPorDia


@pytest.mark.parametrize("tipo, dias, esperado", [
    ("notebook", 3, 30.0),
    ("notebook", 0, 0.0),
    ("notebook", 5, 50.0),
    ("projetor", 2, 30.0),
    ("projetor", 0, 0.0),
    ("projetor", 4, 60.0),
    ("cabo", 5, 10.0),
    ("cabo", 0, 0.0),
    ("cabo", 10, 20.0),
])
def test_calcular_multa_atraso_positivo(tipo, dias, esperado):
    if tipo == "notebook":
        equip = Notebook(1, "Dell", "notebook", MultaPorDia(10.0))
    elif tipo == "projetor":
        equip = Projetor(2, "Epson", "projetor", MultaPorDia(15.0))
    else:
        equip = Cabo(3, "HDMI", "cabo", MultaPorDia(2.0))
    assert equip.calcular_multa(dias) == esperado


@pytest.mark.parametrize("tipo", ["notebook", "projetor", "cabo"])
def test_calcular_multa_atraso_negativo_retorna_zero(tipo):
    if tipo == "notebook":
        equip = Notebook(1, "Dell", "notebook", MultaPorDia(10.0))
    elif tipo == "projetor":
        equip = Projetor(2, "Epson", "projetor", MultaPorDia(15.0))
    else:
        equip = Cabo(3, "HDMI", "cabo", MultaPorDia(2.0))
    assert equip.calcular_multa(-5) == 0.0
    assert equip.calcular_multa(-1) == 0.0
