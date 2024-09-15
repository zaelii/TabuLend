from abc import ABC, abstractmethod

# Interface da Estratégia
class EstrategiaPreco(ABC):
    @abstractmethod
    def calcular_preco(self, dias_aluguel, preco_diario):
        pass

# Estratégia para Preço Normal
class PrecoNormal(EstrategiaPreco):
    def calcular_preco(self, dias_aluguel, preco_diario):
        return 7 * preco_diario # O preço fixo é 7 dias (base)

# Estratégia para Clientes VIP (com desconto)
class PrecoVip(EstrategiaPreco):
    def calcular_preco(self, dias_aluguel, preco_diario):
        desconto = 0.9  # 10% de desconto para clientes VIP
        return dias_aluguel * preco_diario * desconto

# Estratégia para Promoções (por exemplo, aluguel de mais de 7 dias)
class PrecoPromocional(EstrategiaPreco):
    def calcular_preco(self, dias_aluguel, preco_diario):
        if dias_aluguel > 7:
            return dias_aluguel * preco_diario * 0.8  # 20% de desconto para longos períodos
        return dias_aluguel * preco_diario
