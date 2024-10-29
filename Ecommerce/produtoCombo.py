from produto import Produto


class ProdutoCombo(Produto):

    def __init__(self, tipoDesconto, valorDesconto, listaProdutos):
        super().__init__()  # Corrigido para chamar o construtor da classe pai
        self.__tipoDesconto = tipoDesconto
        self.__valorDesconto = valorDesconto
        self.listaProdutos = listaProdutos

    def getPreco(self):
        precoTotal = 0.0
        for produto in self.listaProdutos:
            precoTotal += produto.preco  # Acessando o atributo preco
        # Aplicar desconto
        if self.__tipoDesconto == 'percentual':
            precoTotal -= precoTotal * (self.__valorDesconto / 100)
        else:  # Considerando que o desconto pode ser absoluto
            precoTotal -= self.__valorDesconto

        return precoTotal


