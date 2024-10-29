class ECommerce:
    def __init__(self, listasProdutos, listaClientes, listaPedidos, listaTransportadoras):
        self.__listasProdutos = listasProdutos
        self.__listaClientes = listaClientes
        self.__listaPedidos = listaPedidos
        self.__listaTransportadoras = listaTransportadoras

    def pagar(self, pedido, valor, voucher=None):
        # Se voucher for None, não aplica desconto
        if voucher is None:
            if valor >= pedido.calcularTotal():  # Verifica se o valor é suficiente
                return True
            else:
                return False
        else:
            desconto = 0.10 * pedido.calcularTotal()  # Aplica um desconto de 10%
            if valor >= (pedido.calcularTotal() - desconto):
                return True
            else:
                return False

    def cadastrar(self, cliente):  # Adiciona o cliente na lista de clientes do e-commerce
        self.__listaClientes.append(cliente)

    def comprarProduto(self, produto):  # Adiciona o produto na lista de produtos do e-commerce
        self.__listasProdutos.append(produto)

    def credenciar(self, transportadora):  # Adiciona uma transportadora na lista de transportadoras do e-commerce
        self.__listaTransportadoras.append(transportadora)
