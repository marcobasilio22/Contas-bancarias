
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Executando getter")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome