from pathlib import Path
import json

PASTA = Path(__file__).parent
ARQUIVO = PASTA / "dados.json"
ARQUIVO_PROGRESSO = PASTA / "progresso.json"


def carregar(arquivo=ARQUIVO):
    try:
        with open(arquivo, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def salvar(dados, arquivo=ARQUIVO):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
 