class Carro:
    def __init__(self, marca, modelo, ano, cor, limite_velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 10
        self.ligado = False
        self.velocidade = 0
        self.limite_velocidade = limite_velocidade

    def ligar (self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"O {self.marca} {self.modelo} ligou.")
        else:
            print(f"O {self.marca} {self.modelo} está sem gasolina")

    def desligar (self):
        if self.ligado is True:
            self.ligado = False
            print(f"{self.marca} {self.modelo} desligou.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    def acelerar (self):
        if self.ligado is True:
            if self.combustivel >= 5:
                if self.velocidade <= self.limite_velocidade:
                    self.velocidade += 10
                    self.combustivel -= 5
                    print(f"{self.modelo} acelerou!")
                else:
                    print(f"{self.modelo} está no limite de velocidade")
            else:
                print(f"{self.modelo} está sem combustível.")
        else:
            print(f"{self.modelo} está desligado e não pode acelerar.")

    def frear (self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"{self.modelo} freou, {self.velocidade} km/h.")
        else:
            print(f"{self.modelo} já está parado")

    def abastecer (self, quantidade):
        if self.combustivel + quantidade < 100:
            self.combustivel += quantidade
            print(f"{self.modelo} foi abstecido, combustível: {self.combustivel}")
        else:
            print(f"Abastecimento acima do limite do combustível.")

    def buzinar (self):
        print("BI BI BIIIIIIIIII")

carro1 = Carro ("Mercedes-Benz", "C180", 2020, "Preto", 223)

carro1.acelerar()
carro1.ligar()
carro1.abastecer(80)
for i in range (3):
    carro1.acelerar()
for i in range (1):
    carro1.frear()
carro1.acelerar()
carro1.buzinar()
carro1.desligar()
