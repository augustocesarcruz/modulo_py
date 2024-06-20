class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        print("inicializando classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
         print("Removendo instancia da classe.")

    def falar(self):
            print("Au au")

c = Cachorro("Flora", "Caramelo")
c.falar()