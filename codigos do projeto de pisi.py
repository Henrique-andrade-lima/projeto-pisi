lista_nomes = []
lista_remedios = []
qntd_usuarios = int(input("Digite quantos usuários você deseja cadastrar:"))
for i in range(qntd_usuarios):
    nome = input("Digite seu nome: ")
    lista_nomes.append(nome)
qntd_remedios = int(input("Digite quantos remédios você deseja cadastrar para esse usuário: "))
for i in range(qntd_remedios):
    remedio = ("Digite o nome do remédio que você deseja adicionar para esse usuário: ")
    lista_remedios.append(remedio)

