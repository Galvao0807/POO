class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 20
        self.ligado = False
        self.velocidade = 0

    def ligar (self):
        if self.ligado is False:
            self.ligado = True
            print(f"o carro {self.modelo} ligou.")
        else:
            print(f"O carro {self.modelo} já está ligado.")

    def desligar (self):
        if self.ligado is True:
            self.ligado = False
            print(f"o carro {self.modelo} desligou.")
        else:
            print(f"O carro {self.modelo} já está desligado.")

    def acelerar (self):
        if self.ligado is True:
            if self.combustivel >= 5:
                self.combustivel -= 5
                self.velocidade += 10
                print(f'o {self.modelo} acelerou!')
        else:
            print(f"O carro {self.modelo} está desligado e não pode acelerar.")

    def abastecer (self, quantidade):
        self.combustivel += quantidade
        

        
