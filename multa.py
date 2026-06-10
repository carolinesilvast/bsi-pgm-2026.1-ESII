def calcular_multa_com_carencia(
    dias_atraso,
    dias_carencia,
    valor_por_dia
):
    dias_excedentes = dias_atraso - dias_carencia

    return dias_excedentes * valor_por_dia
