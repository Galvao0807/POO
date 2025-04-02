class ContaBancaria:
    def __init__(self,titular,saldo, limite):
        self.__titular = titular # Privado
        self.__saldo = saldo # Privado
        self.__limite = limite # Privado

    def depositar (self, valor):
        self.__saldo += valor

    def sacar (self, valor):
        pass

    def get_saldo(self):
        return self.__saldo
    
    def set_limite(self, nome_limite):
        pass

conta = ContaBancaria ("Maria", 1000)
print(conta.get_saldo())
print(conta.titular)