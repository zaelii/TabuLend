# sistema_aluguel.py
import random
from jogo import JogoDeTabuleiro
from solicitacao import SolicitacaoAluguel

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
