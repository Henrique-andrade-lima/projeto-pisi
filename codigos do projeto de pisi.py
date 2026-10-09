import json
import re
import time
from datetime import datetime

ARQUIVO = "dados.json"
HORA_REGEX = re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")

# Salvar / carregar
def carregar():
    try:
        with open(ARQUIVO, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
 
 
def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
 
 
# Entradas seguras
def ler_texto(pergunta):
    while True:
        texto = input(pergunta).strip()
        if texto:
            return texto
        print("Não pode ficar vazio.")
 
 
def ler_horarios():
    while True:
        entrada = input("Horários separados por vírgula (ex: 08:00, 14:00, 22:00): ")
        horarios = sorted({h.strip() for h in entrada.split(",") if h.strip()})
        invalidos = [h for h in horarios if not HORA_REGEX.match(h)]
        if horarios and not invalidos:
            return horarios
        print("Horário inválido. Use o formato HH:MM, como 08:00.")
 
 
def escolher_usuario(dados):
    if not dados:
        print("Nenhum usuário cadastrado.")
        return None
    nomes = list(dados)
    for i, nome in enumerate(nomes, start=1):
        print(f"  {i}- {nome}")
    escolha = input("Escolha o número do usuário: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(nomes):
        return nomes[int(escolha) - 1]
    print("Opção inválida.")
    return None

