class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas


    def ligar_motor(self):
        print("Ligando motor...")



class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


#moto = Motocicleta("Azul", "abd-0452", 2)
#moto.ligar_motor()

#carro = Carro("Preto", "apa-5879", 4)
#carro.ligar_motor()

caminhao = Caminhao("verde", "tst-8795", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()