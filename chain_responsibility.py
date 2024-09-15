from abc import ABC, abstractmethod

# Interface do Handler
class AluguelHandler(ABC):
    def __init__(self, proximo=None):
        self._proximo = proximo

    def set_proximo(self, handler):
        self._proximo = handler

    @abstractmethod
    def handle(self, solicitacao):
        if self._proximo:
            return self._proximo.handle(solicitacao)
        return None

# Handler para verificar disponibilidade do jogo
class VerificarDisponibilidade(AluguelHandler):
    def handle(self, solicitacao):
        jogo = solicitacao.jogo
        if not jogo.alugado:
            print(f"O jogo '{jogo.titulo}' está disponível.")
            return super().handle(solicitacao)
        else:
            print(f"O jogo '{jogo.titulo}' já está alugado.")
            return False

# Handler para verificar se o cliente é VIP
class VerificarClienteVIP(AluguelHandler):
    def handle(self, solicitacao):
        cliente = solicitacao.cliente
        if cliente.eh_vip:
            print(f"O cliente '{cliente.nome}' é VIP.")
            return super().handle(solicitacao)
        else:
            print(f"O cliente '{cliente.nome}' não é VIP.")
            return super().handle(solicitacao)

# Classe que gerencia a cadeia de responsabilidade
class CadeiaResponsabilidade:
    def __init__(self):
        # Definindo a cadeia de handlers
        self.disponibilidade = VerificarDisponibilidade()
        self.vip = VerificarClienteVIP()

        # Conectando a cadeia
        self.disponibilidade.set_proximo(self.vip)

    def processar(self, solicitacao):
        return self.disponibilidade.handle(solicitacao)
