from armazenamento import carregar
from usuarios import adicionar_usuarios, remover_usuarios
from remedios import adicionar_remedios, remover_remedio, listar
from alarme import iniciar_alarmes
from placar import mostrar_progresso


def menu():
    dados = carregar()
    opcoes = {
        "1": ("Adicionar usuário", adicionar_usuarios),
        "2": ("Remover usuário", remover_usuarios),
        "3": ("Adicionar remédio a um usuário", adicionar_remedios),
        "4": ("Remover remédio de um usuário", remover_remedio),
        "5": ("Listar tudo", listar),
        "6": ("Iniciar alarme", iniciar_alarmes),
        "7": ("Ver pontos e descontos", mostrar_progresso),
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
            print("Opção inválida. Escolha entre 0 e 7.")


if __name__ == "__main__":
    menu()