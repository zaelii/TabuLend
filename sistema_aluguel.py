import random
from jogo import JogoDeTabuleiro
from solicitacao import SolicitacaoAluguel
from strategy_preco import EstrategiaPreco

class SistemaAluguel:
    _instance = None  # Variável de classe que armazenará a única instância

    @staticmethod
    def getInstance():
        """Método estático responsável por retornar a única instância da classe.
        Se a instância ainda não existir, ele cria uma nova instância.
        Se já existir, retorna a instância existente.
        """
        if SistemaAluguel._instance is None:
            SistemaAluguel._instance = SistemaAluguel(EstrategiaPreco())  # Adiciona a estratégia padrão
        return SistemaAluguel._instance

    def __init__(self, estrategia: EstrategiaPreco):
        """Construtor da classe.
        Garante que, se tentar criar uma nova instância diretamente, o sistema
        lançará uma exceção, assegurando que o Singleton é respeitado.
        """
        if SistemaAluguel._instance is not None:
            raise Exception("Esta classe é um singleton! Use getInstance() para obter a instância.")
        else:
            SistemaAluguel._instance = self
            self.jogos = []                # Lista que armazena todos os jogos disponíveis
            self.solicitacoes = []         # Lista que armazena todas as solicitações de aluguel
            self.estrategia = estrategia   # Estratégia de cálculo de preço

    def set_estrategia(self, estrategia: EstrategiaPreco):
        """Define uma nova estratégia de preço para o sistema."""
        self.estrategia = estrategia

    def calcular_preco(self, dias_aluguel, preco_diario):
        """Calcula o preço de aluguel usando a estratégia definida."""
        preco_total = self.estrategia.calcular_preco(dias_aluguel, preco_diario)
        print(f"O preço total para alugar o jogo por {dias_aluguel} dias é: R$ {preco_total}")
        return preco_total

    def adicionarJogo(self, titulo):
        self.jogos.append(JogoDeTabuleiro(titulo))
        print(f'Jogo "{titulo}" adicionado com sucesso.')

    def exibirJogosDisponiveis(self):
        print("Jogos Disponíveis:")
        for jogo in self.jogos:
            if not jogo.alugado:
                print(f"- {jogo.titulo}")

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

    def exibirSolicitacoesPendentes(self):
        print("Solicitações Pendentes:")
        for solicitacao in self.solicitacoes:
            if solicitacao.status == "Pendente":
                print(f'Cliente: {solicitacao.cliente} | Jogo: {solicitacao.jogo} | Código: {solicitacao.codigoSolicitacao} | Status: {solicitacao.status}')

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

    def recusarSolicitacao(self, codigoSolicitacao):
        for solicitacao in self.solicitacoes:
            if solicitacao.codigoSolicitacao == codigoSolicitacao:
                solicitacao.status = "Recusado"
                print(f'Solicitação recusada para o jogo "{solicitacao.jogo}".')
                return
        print(f'Solicitação com código "{codigoSolicitacao}" não encontrada.')

    def exibirSolicitacoesCliente(self, cliente):
        print(f'Solicitações do Cliente "{cliente}":')
        for solicitacao in self.solicitacoes:
            if solicitacao.cliente == cliente:
                print(f'Jogo: {solicitacao.jogo} | Código: {solicitacao.codigoSolicitacao} | Status: {solicitacao.status}')

    def devolver_jogo(self, titulo):
        for jogo in self.jogos:
            if jogo.titulo == titulo and jogo.alugado:
                jogo.alugado = False
                print(f'O jogo "{titulo}" foi devolvido com sucesso.')
                return
        print(f'O jogo "{titulo}" não está alugado ou não foi encontrado.')
