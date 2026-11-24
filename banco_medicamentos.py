def consolidar(dados):
    """Agrupa os remédios de todos os usuários pelo nome do medicamento."""
    banco = {}
    for usuario, remedios in dados.items():
        for r in remedios:
            nome = r["nome"].strip()
            item = banco.setdefault(nome.casefold(), {"nome": nome, "registros": []})
            item["registros"].append({
                "usuario": usuario,
                "dosagem": r.get("dosagem", ""),
                "tratamento": r.get("tratamento", ""),
                "horarios": r.get("horarios", []),
            })
    return sorted(banco.values(), key=lambda i: i["nome"].casefold())


def listar_todos(dados):
    return consolidar(dados)


def buscar_por_nome(dados, termo):
    termo = termo.strip().casefold()
    return [i for i in consolidar(dados) if termo in i["nome"].casefold()]


def total_registros(dados):
    return sum(len(r) for r in dados.values())