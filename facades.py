# facades.py
from sistema_aluguel import SistemaAluguel

class FacadeCliente:
    def visualizarJogosDisponiveis(self):
        SistemaAluguel.getInstance().exibirJogosDisponiveis()

    def solicitarAluguel(self, cliente, titulo):
        SistemaAluguel.getInstance().solicitarAluguel(cliente, titulo)

    def visualizarSolicitacoes(self, cliente):
        SistemaAluguel.getInstance().exibirSolicitacoesCliente(cliente)

class FacadeAdmin:
    def adicionarJogo(self, titulo):
        SistemaAluguel.getInstance().adicionarJogo(titulo)

    def visualizarSolicitacoesPendentes(self):
        SistemaAluguel.getInstance().exibirSolicitacoesPendentes()

    def aprovarSolicitacao(self, codigoSolicitacao):
        SistemaAluguel.getInstance().aprovarSolicitacao(codigoSolicitacao)

    def recusarSolicitacao(self, codigoSolicitacao):
        SistemaAluguel.getInstance().recusarSolicitacao(codigoSolicitacao)
