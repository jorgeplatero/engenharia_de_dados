
from Animal import Animal


class Gato(Animal):
    def __init__(self):
        super().__init__()
        self.especie = 'Gato'
        self.cor_pelo = 'Branco'
        self.raca = 'Raça'

    def emitir_som(self):
        return 'Miau!'


class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.especie = 'Cachorro'
        self.porte = 'Pequeno'
        self.raca = 'Raça'

    def emitir_som(self):
        return 'Au, au!'


class Coelho(Animal):
    def __init__(self):
        super().__init__()
        self.especie = 'Coelho'
        self.cor_pelo = 'Branco'

    def emitir_som(self):
        return 'O que que há, velhinho?'
    

