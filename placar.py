from entrada import escolher_usuario
from progresso import resumo


def mostrar_progresso(dados):
    nome = escolher_usuario(dados)
    if nome is None:
        return
    r = resumo(nome)
    print(f"\n🏆 Progresso de {nome}")
    print(f"   Pontos: {r['pontos']}")
    print(f"   Dias seguidos: {r['sequencia']}")
    print(f"   Desconto atual: {r['desconto']}%")
    meta = r["proxima_meta"]
    if meta:
        dias_meta, desconto_meta = meta
        faltam = dias_meta - r["sequencia"]
        print(f"   Próxima meta: {dias_meta} dias ({desconto_meta}% de desconto), faltam {faltam} dia(s)")
    else:
        print("   Você atingiu o desconto máximo! 🎉")