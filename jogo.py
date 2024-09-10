# jogo.py
class JogoDeTabuleiro:

    def __init__(self, titulo):
        self.titulo = titulo  # Título do jogo de tabuleiro
        self.alugado = False  # Status de aluguel: True se alugado, False caso contrário (inicia-se disponível)
        self.observadores = [] # lista onde ficara usuarios que querem receber notificação da alteração do jogo 


    def AddObsrvadores(self, observador): # adicionar um observador na lista 
        self.observadores.append(observador)
        print(f'obeservador {observador.nome} adicionado ao jogo {self.titulo}')


    def RemoverObsrvadores(self, observador): # remover um observador na lista 
        self.observadores.remove(observador)

    
    def NotificarObservadores(self): # notifica todos na lista sobre a mudança de estado do jogo
        for observador in self.observadores:
            observador.atualizar(self)
        print(f"Observadores notificados sobre o jogo {self.titulo}")


    def alterarDisponibilidade(self, alugado):  #altera a disponibilidade do jogo para teste
        self.alugado = alugado
        self.NotificarObservadores()



