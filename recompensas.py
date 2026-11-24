from datetime import date, timedelta

PONTOS_POR_DOSE = 10

# (dias seguidos mínimos, desconto em %), do maior para o menor
FAIXAS_DESCONTO = [
    (50, 30),
    (30, 15),
    (20, 10),
    (10, 5),
]


def dia_completo(registro):
    esperadas = set(registro.get("esperadas", []))
    confirmadas = set(registro.get("confirmadas", []))
    return bool(esperadas) and esperadas <= confirmadas


def calcular_sequencia(dias, hoje=None):
    hoje = hoje or date.today()
    dia = hoje
    # Se hoje ainda não está completo, a contagem parte de ontem
    if not dia_completo(dias.get(dia.isoformat(), {})):
        dia -= timedelta(days=1)
    sequencia = 0
    while dia_completo(dias.get(dia.isoformat(), {})):
        sequencia += 1
        dia -= timedelta(days=1)
    return sequencia


def calcular_desconto(sequencia):
    for minimo, desconto in FAIXAS_DESCONTO:
        if sequencia >= minimo:
            return desconto
    return 0


def proxima_meta(sequencia):
    for minimo, desconto in reversed(FAIXAS_DESCONTO):
        if sequencia < minimo:
            return minimo, desconto
    return None


def calcular_pontos(dias):
    total = sum(len(r.get("confirmadas", [])) for r in dias.values())
    return total * PONTOS_POR_DOSE