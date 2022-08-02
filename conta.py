
class Conta:

    print("Bem vindo ao banco Mdb Soluctions! Por gentileza, preencha os seguintes dados: numero, titular, saldo, limite")

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"


    def extrato(self):
        print("O valor disponível é de {} na conta do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor   )):
              self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}