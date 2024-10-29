class Produto:
    def __init__(self, nome, preco, volume, peso):
        self.__nome = nome
        self.__preco = preco
        self.__volume = volume
        self.__peso = peso

    def getNome(self):
        return self.__nome

    def getPreco(self):
        return self.__preco

    def getVolume(self):
        return self.__volume

    def getPeso(self):
        return self.__peso

    def __str__(self):
        return f"Produto(nome={self.getNome()}, preco={self.getPreco()}, volume={self.getVolume()}, peso={self.getPeso()})"
