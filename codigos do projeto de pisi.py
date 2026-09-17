lista_nomes = []
lista_remedios = []
qntd_usuarios = int(input("Digite quantos usuários você deseja cadastrar:"))
for i in range(qntd_usuarios):
    nome = input("Digite o nome que você deseja adicionar: ")
    lista_nomes.append(nome)
qntd_remedios = int(input("Digite quantos remédios você deseja cadastrar para esse usuário: "))
for i in range(qntd_remedios):
    remedio = ("Digite o nome do remédio que você deseja adicionar para esse usuário: ")
    lista_remedios.append(remedio)

modificacoes = int(input("1- Você deseja adicionar um usuário?(digite 1) 2- Você não deseja alterar nada?(digite 2) 3- Você deseja remover um usuário?(digite 3): "))
if modificacoes == 1:
    novo_usuario = input("Digite o nome do nome do novo usuário: ")
    lista_nomes.append(novo_usuario)
elif modificacoes == 2:
    print("Você não fez alterações.")
elif modificacoes == 3:
    remover_usuario = input("Digite o nome que você deseja remover: ")
    lista_nomes.remove(remover_usuario)
    if remover_usuario not in lista_nomes:
        print("Esse nome não está cadastrado.")
else:
    print("Não existe essa opção. Escolha entre as opções 1 a 3.")
    