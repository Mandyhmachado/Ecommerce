from produto import Produto
from pedido import Pedido
from item import Item
from endereco import Endereco
from ecommerce import ECommerce

# Instanciando produtos
produto1 = Produto("Capa", 5.5, 2, 0.5)
produto2 = Produto("Carregador", 10.00, 5, 0.200)
produto3 = Produto("Fone de ouvido", 5.0, 0.10, 0.100)
produto4 = Produto("Suporte", 2.0, 0.330, 0.330)
produto5 = Produto("Película", 10.00, 154, 0.200)

# Instanciando endereços
endereco1 = Endereco("Santo Amaro", "Passagem", 127, "Casa Azul")
endereco2 = Endereco("Alcindo Cancela", "Travessa", 500, "Prédio")
endereco3 = Endereco("Pedromiranda", "Avenida", 732, "Cao lado da cafeteria")

# Instanciando pedidos
pedido1 = Pedido("Ana", endereco1, "Sedex")
pedido2 = Pedido("Pedro", endereco2, "Correios")

# Instanciando itens
item1 = Item(2, produto1)  # Usando o objeto produto1
item2 = Item(1, produto3)  # Usando o objeto produto3
item3 = Item(5, produto2)  # Usando o objeto produto2

# Adicionando itens aos pedidos
pedido1.adicionar(item1)  # Adiciona item1 ao pedido1
pedido1.adicionar(item2)  # Adiciona item2 ao pedido1
pedido2.adicionar(item3)  # Adiciona item3 ao pedido2

# Instanciando o Ecommerce
ufraCommerce = ECommerce([produto1, produto2, produto3, produto4, produto5],
                         ["João", "Maria", "Ana"],
                         [pedido1, pedido2],
                         ["Sedex", "Correios"])

