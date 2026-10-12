from pathlib import Path
import json
import re
import time
from datetime import datetime

ARQUIVO = Path(__file__).with_name("dados.json")
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

# Funcionalidades do app
def adicionar_usuarios(dados):
    nome = ler_texto("Nome do novo usuário:")
    if nome in dados:
        print("Esse usuário já foi cadastrado.")
        return
    dados[nome] = []
    salvar(dados)
    print(f"Usuário/a {nome} cadastrado")

def remover_usuarios(dados):
    nome = escolher_usuario(dados)
    if nome is None:
        return
    if input(f"Remover {nome} e todos os remédios? (s/n):").lower() == "s":
        del dados[nome]
        salvar(dados)
        print("Usuário removido do sistema com sucesso!")

def adicionar_remedios(dados):
    nome_usuario = escolher_usuario(dados)
    if nome_usuario is None:
        return
    remedio = {"nome": ler_texto("Nome do remédio: "), "dosagem": input("Dosagem (ex: 100 mg):").strip(), "tratamento": input("Qual problema está sendo tratado: ").strip(), "horarios": ler_horarios(),}
    dados[nome_usuario].append(remedio)
    salvar(dados)
    print(f"Remédio {remedio['nome']} adicionado para {nome_usuario}.")

def remover_remedio(dados):
    nome_usuario = escolher_usuario(dados)
    if nome_usuario is None:
        return
    remedios = dados[nome_usuario]
    if not remedios:
        print("Esse usuário não tem remédios.")
        return
    for i, r in enumerate(remedios, start=1):
        print(f"  {i}- {r['nome']}")
    escolha = input("Número do remédio a remover: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(remedios):
        removido = remedios.pop(int(escolha) - 1)
        salvar(dados)
        print(f"{removido['nome']} removido.")
    else:
        print("Opção inválida.")

def listar(dados):
    if not dados:
        print("Nada cadastrado ainda.")
        return
    for nome, remedios in dados.items():
        print(f"\n👤 {nome}")
        if not remedios:
            print("   (sem remédios)")
        for r in remedios:
            print(f"   💊 {r['nome']} - {r['dosagem'] or 'sem dosagem'}")
            print(f"      Tratamento: {r['tratamento'] or 'não informado'}")
            print(f"      Horários: {', '.join(r['horarios'])}")

def iniciar_alarmes(dados):
    print("Alarme ativo! Pressione Cntrl+C ou [voltar] para voltar ao menu.")
    avisados = set() #Evita o aviso ser repetido no mesmo minuto
    try:
        while True:
            agora = datetime.now()
            hhmm = agora.strftime("%H:%M")
            for nome, remedios in dados.items():
                for r in remedios:
                    chave = (agora.date(), nome, r["nome"], hhmm)
                    if hhmm in r["horarios"] and chave not in avisados:
                        avisados.add(chave)
                        print(f"\a\a\a⏰ {hhmm} - {nome}: tomar {r['nome']} ({r['dosagem'] or 'sem dosagem'})")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nAlarme encerrado.")

#opções no menu
def menu():
    dados = carregar()
    opcoes = {
        "1": ("Adicionar usuário", adicionar_usuarios),
        "2": ("Remover usuário", remover_usuarios),
        "3": ("Adicionar remédio a um usuário", adicionar_remedios),
        "4": ("Remover remédio de um usuário", remover_remedio),
        "5": ("Listar tudo", listar),
        "6": ("Iniciar alarme", iniciar_alarmes),
        "0": ("Sair", None),
    }
    while True:
        print("\n=== Gerenciador de Remédios ===")
        for chave, (texto, _) in opcoes.items():
            print(f"{chave}- {texto}")
        escolha = input("Escolha: ").strip()
        if escolha == "0":
            print("Até mais!")
            break
        if escolha in opcoes:
            opcoes[escolha][1](dados)
        else:
            print("Opção inválida. Escolha entre 0 e 6.")


if __name__ == "_main_":
    menu()