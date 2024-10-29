from datetime import datetime

class Pedido:
    def __init__(self, cliente, endereco, transportadora):
        self.__dataEhora = datetime.now()  # Define a data e hora automaticamente
        self.__subtotal = 0.0
        self.__frete = 0.0
        self.__total = 0.0
        self.cliente = cliente
        self.endereco = endereco
        self.transportadora = transportadora
        self.listaItens = []

    def calcularTotal(self):
        self.__total = self.__subtotal + self.__frete

    def adicionarProduto(self, produto, quantidade=1):
        for item in self.listaItens:
            if item[0] == produto:  # item[0] é o produto
                item[1] += quantidade  # Incrementa a quantidade
                break
        else:
            self.listaItens.append((produto, quantidade))  # Adiciona novo produto

        self.__calcularSubtotal()  # Atualiza subtotal após adicionar produto
        self.__calcularFrete()  # Atualiza frete após adicionar produto
        self.calcularTotal()  # Atualiza total

    def __calcularFrete(self):
        self.__frete = self.transportadora.calcularFrete(self.listaItens)  # Passa a lista de itens

    def setTransportadora(self, transportadora):
        self.transportadora = transportadora
        self.__calcularFrete()  # Atualiza frete ao mudar transportadora

    def remover(self, produto):
        for i, item in enumerate(self.listaItens):
            if item[0] == produto:  # item[0] é o produto
                del self.listaItens[i]
                print("Produto removido")
                self.__calcularSubtotal()  # Atualiza subtotal após remoção
                self.__calcularFrete()  # Atualiza frete após remoção
                self.calcularTotal()  # Atualiza total
                break
        else:
            print("Não há como remover o item com o produto indicado")

    def __calcularSubtotal(self):
        self.__subtotal = sum(item[0].getPreco() * item[1] for item in self.listaItens)  # Calcula subtotal
A