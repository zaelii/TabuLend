# jogo.py
class JogoDeTabuleiro:

    def __init__(self, titulo, preco=0):
        self.titulo = titulo  # Título do jogo de tabuleiro
        self.preco = preco  # Preço do jogo
        self.alugado = False  # Status de aluguel: True se alugado, False caso contrário (inicia-se disponível)
        self.observadores = []  # Lista onde ficarão usuários que querem receber notificação da alteração do jogo

    def AddObsrvadores(self, observador):  # Adicionar um observador na lista
        self.observadores.append(observador)
        print(f'Observador {observador.nome} adicionado ao jogo {self.titulo}')

    def RemoverObsrvadores(self, observador):  # Remover um observador na lista
        self.observadores.remove(observador)

    def NotificarObservadores(self):  # Notifica todos na lista sobre a mudança de estado do jogo
        for observador in self.observadores:
            observador.atualizar(self)
        print(f"Observadores notificados sobre o jogo {self.titulo}")

    def alterarDisponibilidade(self, alugado):  # Altera a disponibilidade do jogo
        self.alugado = alugado
        self.NotificarObservadores()

    def calcular_preco(self):
        """Método que retorna o preço do jogo."""
        return self.preco

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Preço: R$ {self.preco}, Status: {'Alugado' if self.alugado else 'Disponível'}")
