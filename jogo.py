# jogo.py
class Jogo:

    def __init__(self, titulo, editora,preco,status):
        self.titulo = titulo  # Título do jogo de tabuleiro
        self.editora = editora
        self.preco = preco  # Preço do jogo
        self.status = status
        self.observadores = []  # Lista onde ficarão usuários que querem receber notificação da alteração do jogo

    def AddObsrvadores(self, observador):  # Adiciona um observador na lista
        self.observadores.append(observador)
        print(f'Observador {observador.nome} adicionado ao jogo {self.titulo}')

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

    def catalogoJogos():
            jogos = []
            try:
                with open('catalogoJogos.txt', 'r') as file:
                    for line in file:
                        line = line.strip()
                        if line:  # Verifica se a linha não está vazia
                            # Divide a linha em partes usando ', ' como delimitador
                            parts = line.split(', ')
                            if len(parts) == 4:
                                try:
                                    titulo = parts[0].split(': ')[1]
                                    editora = parts[1].split(': ')[1]
                                    preco = parts[2].split(': ')[1]
                                    status = parts[3].split(': ')[1]
                                    jogos.append(Jogo(titulo, editora, preco, status))
                                except IndexError:
                                    print(f"Erro ao processar linha: {line}")
            except FileNotFoundError:
                print("Arquivo de catálogo de jogos não encontrado.")
            return jogos
    
    def salvarJogo(self):
        with open('catalogoJogos.txt', 'a') as file:
            file.write(f"titulo: {self.titulo}, editora: {self.editora}, Valor: {self.preco}, status: {self.status}\n")
