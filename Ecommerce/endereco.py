class Endereco:
    def __init__(self, nome, logradouro, numero, complemento):
        self.__nome = nome
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getLogradouro(self):
        return self.__logradouro

    def setLogradouro(self, logradouro):
        self.__logradouro = logradouro

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero

    def getComplemento(self):
        return self.__complemento

    def setComplemento(self, complemento):
        self.__complemento = complemento
