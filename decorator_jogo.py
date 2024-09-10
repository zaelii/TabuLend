# decorator_jogo.py
class JogoDecorator:
    """Classe base para o Decorator."""
    def __init__(self, jogo):
        self.jogo = jogo

    def calcular_preco(self):
        """Encapsula o comportamento do cálculo de preço."""
        return self.jogo.calcular_preco()

    def exibir_detalhes(self):
        """Encapsula a exibição dos detalhes do jogo."""
        self.jogo.exibir_detalhes()


class JogoComDesconto(JogoDecorator):
    """Decorator para aplicar um desconto ao preço do jogo."""
    def __init__(self, jogo, desconto):
        super().__init__(jogo)
        self.desconto = desconto

    def calcular_preco(self):
        """Calcula o preço com desconto."""
        preco_original = self.jogo.calcular_preco()
        return preco_original * (1 - self.desconto)

    def exibir_detalhes(self):
        """Exibe os detalhes do jogo, incluindo o preço com desconto."""
        super().exibir_detalhes()
        print(f"Preço com desconto: R$ {self.calcular_preco():.2f} (Desconto de {self.desconto * 100}%)")
