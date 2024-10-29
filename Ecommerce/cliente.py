class Cliente:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email
