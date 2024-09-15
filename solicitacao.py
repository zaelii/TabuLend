# solicitacao.py
class SolicitacaoAluguel:
    def __init__(self, cliente, jogo, codigo):
        self.cliente = cliente      # Nome do cliente que fez a solicitação
        self.jogo = jogo            # Título do jogo solicitado
        self.status = "Pendente"    # Status da solicitação: "Pendente", "Aprovado", "Recusado"
        self.codigoSolicitacao = codigo  # Código único da solicitação de aluguel

    def aprovar(self):
        self.status = "Aprovado"

    def recusar(self):
        self.status = "Recusado"
