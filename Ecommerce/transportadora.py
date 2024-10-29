class Transportadora:
    def __init__(self, nome, precoVolume, precoPeso, prazoEntrega):
        self.__nome = nome
        self.__precoVolume = precoVolume
        self.__precoPeso = precoPeso
        self.__prazoEntrega = prazoEntrega

    def calcularFrete(self, itens):
        total_frete = 0.0

        for item in itens:
            produto, quantidade = item  # Desempacota o produto e a quantidade
            volume = produto.volume  # Assume que o produto tem um atributo 'volume'
            peso = produto.peso  # Assume que o produto tem um atributo 'peso'

            # Calcula o frete por volume e por peso
            frete_por_volume = self.__precoVolume * volume * quantidade
            frete_por_peso = self.__precoPeso * peso * quantidade

            # Adiciona o maior valor entre frete por volume e por peso
            total_frete += max(frete_por_volume, frete_por_peso)

        return total_frete