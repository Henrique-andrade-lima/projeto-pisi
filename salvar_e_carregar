from pathlib import Path
import json

ARQUIVO = Path(__file__).with_name("dados.json")

def carregar():
    try:
        with open(ARQUIVO, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
 
 
def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
 