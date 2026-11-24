from datetime import date

from armazenamento import carregar, salvar, ARQUIVO_PROGRESSO
from recompensas import (
    calcular_sequencia,
    calcular_desconto,
    calcular_pontos,
    proxima_meta,
)


def _id_dose(remedio, horario):
    return f"{remedio}|{horario}"


def _doses_agendadas(remedios):
    return sorted({_id_dose(r["nome"], h) for r in remedios for h in r["horarios"]})


def registrar_confirmacao(usuario, remedios, remedio, horario, hoje=None):
    hoje = hoje or date.today()
    progresso = carregar(ARQUIVO_PROGRESSO)
    dias = progresso.setdefault(usuario, {})
    registro = dias.setdefault(hoje.isoformat(), {"esperadas": [], "confirmadas": []})
    registro["esperadas"] = _doses_agendadas(remedios)
    dose = _id_dose(remedio, horario)
    if dose not in registro["confirmadas"]:
        registro["confirmadas"].append(dose)
    salvar(progresso, ARQUIVO_PROGRESSO)


def resumo(usuario):
    dias = carregar(ARQUIVO_PROGRESSO).get(usuario, {})
    sequencia = calcular_sequencia(dias)
    return {
        "pontos": calcular_pontos(dias),
        "sequencia": sequencia,
        "desconto": calcular_desconto(sequencia),
        "proxima_meta": proxima_meta(sequencia),
    }


def apagar_usuario(usuario):
    progresso = carregar(ARQUIVO_PROGRESSO)
    if usuario in progresso:
        del progresso[usuario]
        salvar(progresso, ARQUIVO_PROGRESSO)