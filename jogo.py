
class JogoDeTabuleiro:

    def __init__(self, titulo, editora,preco,status,imagem):
        self.titulo = titulo  # Título do jogo de tabuleiro
        self.editora = editora
        self.preco = preco  # Preço do jogo
        self.status = status
        self.imagem = imagem
        self.observadores = []  # Lista onde ficarão usuários que querem receber notificação da alteração do jogo

    def AddObsrvadores(self, observador):  # Adiciona um observador na lista
        self.observadores.append(observador)

    def RemoverObsrvadores(self, observador):  # Remove um observador da lista
        self.observadores.remove(observador)

    def NotificarObservadores(self):  # Notifica todos da lista sobre a disponibilidade do jogo
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

    @staticmethod
    def catalogoJogos():
        jogos = []
        try:
            with open('catalogoJogos.txt', 'r') as file:
                for line in file:
                    partes = line.strip().split(', ')
                    titulo = partes[0].split(': ')[1]
                    editora = partes[1].split(': ')[1]
                    preco = partes[2].split(': ')[1]
                    status = partes[3].split(': ')[1]
                    imagem = partes[4].split(': ')[1] if len(partes) > 4 else None
                    jogos.append(JogoDeTabuleiro(titulo, editora, preco, status, imagem))
        except FileNotFoundError:
            print("Arquivo de catálogo de jogos não encontrado.")
        return jogos

    def salvarJogo(self):
        with open('catalogoJogos.txt', 'a') as file:
            file.write(f"titulo: {self.titulo}, editora: {self.editora}, preco: {self.preco}, status: {self.status}, imagem: {self.imagem}\n")