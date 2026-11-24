from banco_medicamentos import listar_todos, buscar_por_nome, total_registros


def _mostrar(itens):
    if not itens:
        print("Nenhum medicamento encontrado.")
        return
    for item in itens:
        qtd = len(item["registros"])
        print(f"\n💊 {item['nome']} (usado por {qtd} {'usuário' if qtd == 1 else 'usuários'})")
        for reg in item["registros"]:
            print(f"   👤 {reg['usuario']}")
            print(f"      Dosagem: {reg['dosagem'] or 'sem dosagem'}")
            print(f"      Tratamento: {reg['tratamento'] or 'não informado'}")
            print(f"      Horários: {', '.join(reg['horarios'])}")
    print(f"\n{len(itens)} medicamento(s) listado(s).")


def consultar_medicamentos(dados):
    while True:
        print("\n=== Banco de Medicamentos ===")
        print("1- Ver todos os medicamentos cadastrados")
        print("2- Buscar por nome")
        print("0- Voltar")
        escolha = input("Escolha: ").strip()
        if escolha == "1":
            if total_registros(dados) == 0:
                print("Nenhum medicamento cadastrado ainda.")
            else:
                _mostrar(listar_todos(dados))
        elif escolha == "2":
            termo = input("Nome (ou parte do nome): ").strip()
            if termo:
                _mostrar(buscar_por_nome(dados, termo))
            else:
                print("Digite pelo menos uma letra.")
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Escolha entre 0 e 2.")