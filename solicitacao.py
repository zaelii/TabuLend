import uuid  # Biblioteca para geração de identificadores únicos


class SolicitacaoAluguel:
    def __init__(self, cliente, jogo, codigo):
        self.cliente = cliente      # Nome do cliente que fez a solicitação
        self.jogo = jogo            # Título do jogo solicitado
        self.preco = 0              # Preço do aluguel
        self.status = "Pendente"    # Status da solicitação: "Pendente", "Aprovado", "Recusado"
        self.codigo = self.gerar_codigo_solicitacao()  # Gera um código único para a solicitação

    def aprovar(self):
        self.status = "Aprovado"

    def recusar(self):
        self.status = "Recusado"

    def gerar_codigo_solicitacao(self):
        return str(uuid.uuid4())  # Gera um UUID como string