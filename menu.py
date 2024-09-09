from facades import *

def main():
    clienteFacade = FacadeCliente()
    adminFacade = FacadeAdmin()
    menu(True)

def modoCliente(clienteFacade):
    while True:
        print("\nModo Cliente")
        print("1. Visualizar Jogos Disponíveis")
        print("2. Solicitar Aluguel de Jogo")
        print("3. Visualizar Solicitações")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            clienteFacade.visualizarJogosDisponiveis()
        elif opcao == '2':
            clienteNome = input("Digite seu nome: ")
            titulo = input("Digite o título do jogo para alugar: ")
            clienteFacade.solicitarAluguel(clienteNome, titulo)
        elif opcao == '3':
            clienteNome = input("Digite seu nome: ")
            clienteFacade.visualizarSolicitacoes(clienteNome)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def modoAdmin(adminFacade):
    while True:
        print("\nModo Administrador")
        print("1. Adicionar Jogo")
        print("2. Visualizar Solicitações Pendentes")
        print("3. Aprovar Solicitação")
        print("4. Recusar Solicitação")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do jogo: ")
            adminFacade.adicionarJogo(titulo)
        elif opcao == '2':
            adminFacade.visualizarSolicitacoesPendentes()
        elif opcao == '3':
            codigo = input("Digite o código de solicitação para aprovar: ")
            adminFacade.aprovarSolicitacao(codigo)
        elif opcao == '4':
            codigo = input("Digite o código de solicitação para recusar: ")
            adminFacade.recusarSolicitacao(codigo)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
 
def menu():
    while True:
        print("\nSistema de Aluguel de Jogos de Tabuleiro")
        print("1. Entrar como Cliente")
        print("2. Entrar como Administrador")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            clienteFacade = FacadeCliente()
            modoCliente(clienteFacade)

        elif opcao == '2':
            adminFacade = FacadeAdmin()
            modoAdmin(adminFacade)
            
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


