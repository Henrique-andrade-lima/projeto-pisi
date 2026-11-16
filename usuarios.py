from armazenamento import salvar
from entrada import ler_texto, escolher_usuario


def adicionar_usuarios(dados):
    nome = ler_texto("Nome do novo usuário: ")
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
    if input(f"Remover {nome} e todos os remédios? (s/n): ").lower() == "s":
        del dados[nome]
        salvar(dados)
        print("Usuário removido do sistema com sucesso!")