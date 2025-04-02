class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.quantidade = quantidade

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print ("Não é permitido valor negativo!")


produto1 = Produto("Caneta", 1, 300)
# print(produto1.get_nome())
# print("Tentando modificar o nome do produto")
# novoNomeProduto = input("Digite o nome do produto: ")
# produto1.set_nome(novoNomeProduto)
# print("Nome do produto: ")
# print(produto1.get_nome())
novoPreco = float(input("Digite o novo preço do produto: "))
produto1.set_preco(novoPreco)


print(f"Preço do {produto1.get_nome()}: {produto1.get_preco()}")