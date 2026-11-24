from banco_medicamentos import (
    listar_todos,
    listar_categorias,
    buscar_por_nome,
    buscar_por_categoria,
)


def _mostrar(lista):
    if not lista:
        print("Nenhum medicamento encontrado.")
        return
    for m in lista:
        print(f"\n💊 {m['nome']}")
        print(f"   Categoria: {m['categoria']}")
        print(f"   Uso comum: {m['uso']}")
        print(f"   Venda: {m['venda']}")
    print(f"\n{len(lista)} medicamento(s) listado(s).")


def _escolher_categoria():
    categorias = listar_categorias()
    for i, c in enumerate(categorias, start=1):
        print(f"  {i}- {c}")
    escolha = input("Número da categoria: ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(categorias):
        return categorias[int(escolha) - 1]
    print("Opção inválida.")
    return None


def consultar_medicamentos(dados=None):
    # "dados" não é usado; existe só para combinar com as outras opções do menu
    while True:
        print("\n=== Banco de Medicamentos ===")
        print("1- Ver todos")
        print("2- Buscar por nome")
        print("3- Ver por categoria")
        print("0- Voltar")
        escolha = input("Escolha: ").strip()
        if escolha == "1":
            _mostrar(listar_todos())
        elif escolha == "2":
            termo = input("Nome (ou parte do nome): ").strip()
            if termo:
                _mostrar(buscar_por_nome(termo))
            else:
                print("Digite pelo menos uma letra.")
        elif escolha == "3":
            categoria = _escolher_categoria()
            if categoria:
                _mostrar(buscar_por_categoria(categoria))
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Escolha entre 0 e 3.")
    print("\nInformação apenas de consulta. Siga sempre a orientação médica e a bula.")