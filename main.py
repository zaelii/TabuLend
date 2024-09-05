import random
#cheguei aqui
# Classe representando um jogo de tabuleiro
class JogoDeTabuleiro:
    def __init__(self, titulo):
        self.titulo = titulo  # Título do jogo de tabuleiro
        self.alugado = False  # Status de aluguel: True se alugado, False caso contrário

# Classe representando uma solicitação de aluguel
class SolicitacaoAluguel:
    def __init__(self, cliente, jogo, codigo):
        self.cliente = cliente      # Nome do cliente que fez a solicitação
        self.jogo = jogo            # Título do jogo solicitado
        self.status = "Pendente"    # Status da solicitação: "Pendente", "Aprovado", "Recusado"
        self.codigoSolicitacao = codigo  # Código único da solicitação de aluguel

# Singleton SistemaAluguel - Gerencia o acervo de jogos e as solicitações de aluguel
class SistemaAluguel:
    _instance = None

    @staticmethod
    def getInstance():
        if SistemaAluguel._instance is None:
            SistemaAluguel()
        return SistemaAluguel._instance

    def __init__(self):
        if SistemaAluguel._instance is not None:
            raise Exception("Esta classe é um singleton!")
        else:
            SistemaAluguel._instance = self
            self.jogos = []                # Lista que armazena todos os jogos disponíveis
            self.solicitacoes = []         # Lista que armazena todas as solicitações de aluguel

    # Adiciona um novo jogo ao acervo
    def adicionarJogo(self, titulo):
        self.jogos.append(JogoDeTabuleiro(titulo))
        print(f'Jogo "{titulo}" adicionado com sucesso.')

    # Exibe todos os jogos disponíveis para aluguel
    def exibirJogosDisponiveis(self):
        print("Jogos Disponíveis:")
        for jogo in self.jogos:
            if not jogo.alugado:
                print(f"- {jogo.titulo}")

    # Solicita o aluguel de um jogo específico
    def solicitarAluguel(self, cliente, titulo):
        for jogo in self.jogos:
            if jogo.titulo == titulo:
                if not jogo.alugado:
                    codigoSolicitacao = f'SOL-{random.randint(1000, 9999)}'
                    self.solicitacoes.append(SolicitacaoAluguel(cliente, titulo, codigoSolicitacao))
                    print(f'Solicitação de aluguel para "{titulo}" feita com sucesso.')
                    print(f'Código de Solicitação gerado: {codigoSolicitacao}')
                    return
                else:
                    print(f'Jogo "{titulo}" já está alugado.')
                    return
        print(f'Jogo "{titulo}" não encontrado.')

    # Exibe todas as solicitações pendentes de aprovação
    def exibirSolicitacoesPendentes(self):
        print("Solicitações Pendentes:")
        for solicitacao in self.solicitacoes:
            if solicitacao.status == "Pendente":
                print(f'Cliente: {solicitacao.cliente} | Jogo: {solicitacao.jogo} | Código: {solicitacao.codigoSolicitacao} | Status: {solicitacao.status}')

    # Aprova uma solicitação de aluguel com base no código de solicitação
    def aprovarSolicitacao(self, codigoSolicitacao):
        for solicitacao in self.solicitacoes:
            if solicitacao.codigoSolicitacao == codigoSolicitacao:
                for jogo in self.jogos:
                    if jogo.titulo == solicitacao.jogo:
                        jogo.alugado = True
                        solicitacao.status = "Aprovado"
                        print(f'Solicitação aprovada para o jogo "{solicitacao.jogo}".')
                        return
        print(f'Solicitação com código "{codigoSolicitacao}" não encontrada.')

    # Recusa uma solicitação de aluguel com base no código de solicitação
    def recusarSolicitacao(self, codigoSolicitacao):
        for solicitacao in self.solicitacoes:
            if solicitacao.codigoSolicitacao == codigoSolicitacao:
                solicitacao.status = "Recusado"
                print(f'Solicitação recusada para o jogo "{solicitacao.jogo}".')
                return
        print(f'Solicitação com código "{codigoSolicitacao}" não encontrada.')

    # Exibe todas as solicitações feitas por um cliente específico
    def exibirSolicitacoesCliente(self, cliente):
        print(f'Solicitações do Cliente "{cliente}":')
        for solicitacao in self.solicitacoes:
            if solicitacao.cliente == cliente:
                print(f'Jogo: {solicitacao.jogo} | Código: {solicitacao.codigoSolicitacao} | Status: {solicitacao.status}')

# Façade para o cliente - Interface simplificada para o cliente interagir com o sistema
class FacadeCliente:
    def visualizarJogosDisponiveis(self):
        SistemaAluguel.getInstance().exibirJogosDisponiveis()

    def solicitarAluguel(self, cliente, titulo):
        SistemaAluguel.getInstance().solicitarAluguel(cliente, titulo)

    def visualizarSolicitacoes(self, cliente):
        SistemaAluguel.getInstance().exibirSolicitacoesCliente(cliente)

# Façade para o administrador - Interface simplificada para o administrador interagir com o sistema
class FacadeAdmin:
    def adicionarJogo(self, titulo):
        SistemaAluguel.getInstance().adicionarJogo(titulo)

    def visualizarSolicitacoesPendentes(self):
        SistemaAluguel.getInstance().exibirSolicitacoesPendentes()

    def aprovarSolicitacao(self, codigoSolicitacao):
        SistemaAluguel.getInstance().aprovarSolicitacao(codigoSolicitacao)

    def recusarSolicitacao(self, codigoSolicitacao):
        SistemaAluguel.getInstance().recusarSolicitacao(codigoSolicitacao)

# Função para modo Cliente
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

# Função para modo Administrador
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

# Função principal
def main():
    clienteFacade = FacadeCliente()
    adminFacade = FacadeAdmin()

    while True:
        print("\nSistema de Aluguel de Jogos de Tabuleiro")
        print("1. Entrar como Cliente")
        print("2. Entrar como Administrador")
        print("3. Sair")
        # Escolha do modo de operação
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            modoCliente(clienteFacade)
        elif opcao == '2':
            modoAdmin(adminFacade)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
