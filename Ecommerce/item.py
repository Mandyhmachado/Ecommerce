from produto import Produto

class Item:
    def __init__(self, quantidade, produto: Produto):
        self.__quantidade = quantidade
        self.__subtotal = 0.0  # Inicializando subtotal
        self.produto = produto
        self.__calcularSubtotal()  # Chama o método privado para calcular subtotal

    def __calcularSubtotal(self):
        self.__subtotal = self.__quantidade * self.produto.getPreco()  # Usando o método getter para acessar o preço

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade  # Atualiza o atributo privado
        self.__calcularSubtotal()  # Recalcula o subtotal

    def getSubtotal(self):
        return self.__subtotal  # Método getter para subtotal

    def getQuantidade(self):
        return self.__quantidade  # Método getter para quantidade
