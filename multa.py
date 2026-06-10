def calcular_multa_com_carencia(
    dias_atraso,
    dias_carencia,
    valor_por_dia
):
    dias_excedentes = max(
        0,
        dias_atraso - dias_carencia
    )

    multa = dias_excedentes * valor_por_dia

    return round(multa, 2)
