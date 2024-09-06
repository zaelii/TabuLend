# Lista para armazenar os jogos
catalogo_jogos = []

# Função para adicionar um jogo ao catálogo
def adicionar_jogo(nome, editora, preco, dias_aluguel):
    jogo = {
        'nome': nome,
        'editora': editora,
        'preco': preco,
        'dias_aluguel': dias_aluguel,
        'disponivel': True  # Inicialmente, o jogo está disponível para aluguel
    }
    catalogo_jogos.append(jogo)
    print(f"Jogo '{nome}' adicionado ao catálogo com sucesso!")

# Função para listar os jogos no catálogo
def listar_jogos():
    if not catalogo_jogos:
        print("Nenhum jogo no catálogo.")
    else:
        print("Catálogo de Jogos Disponíveis:")
        for i, jogo in enumerate(catalogo_jogos):
            status = "Disponível" if jogo['disponivel'] else "Alugado"
            print(f"{i + 1}. Nome: {jogo['nome']}, Editora: {jogo['editora']}, Preço: R$ {jogo['preco']}, Dias: {jogo['dias_aluguel']}, Status: {status}")

# Função para alugar um jogo
def alugar_jogo(indice):
    if 0 <= indice < len(catalogo_jogos):
        jogo = catalogo_jogos[indice]
        if jogo['disponivel']:
            jogo['disponivel'] = False
            print(f"Você alugou o jogo '{jogo['nome']}' por {jogo['dias_aluguel']} dias.")
        else:
            print(f"O jogo '{jogo['nome']}' já está alugado.")
    else:
        print("Índice inválido. Escolha um jogo válido.")

# Função para devolver um jogo alugado
def devolver_jogo(indice):
    if 0 <= indice < len(catalogo_jogos):
        jogo = catalogo_jogos[indice]
        if not jogo['disponivel']:
            jogo['disponivel'] = True
            print(f"Você devolveu o jogo '{jogo['nome']}'.")
        else:
            print(f"O jogo '{jogo['nome']}' já está disponível.")
    else:
        print("Índice inválido. Escolha um jogo válido.")

# Função para solicitar informações e adicionar um novo jogo
def adicionar_jogo_via_input():
    nome = input("Nome do Jogo: ")
    editora = input("Editora: ")
    preco = float(input("Preço: R$ "))
    dias_aluguel = int(input("Dias de Aluguel: "))
    adicionar_jogo(nome, editora, preco, dias_aluguel)

# Função principal para interagir com o usuário
def menu_principal():
    while True:
        print("\n1. Adicionar Jogo")
        print("2. Listar Jogos")
        print("3. Alugar Jogo")
        print("4. Devolver Jogo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_jogo_via_input()
        elif opcao == '2':
            listar_jogos()
        elif opcao == '3':
            listar_jogos()
            indice = int(input("Digite o número do jogo para alugar: ")) - 1
            alugar_jogo(indice)
        elif opcao == '4':
            listar_jogos()
            indice = int(input("Digite o número do jogo para devolver: ")) - 1
            devolver_jogo(indice)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Iniciar o sistema
menu_principal()
