class Animal:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.especie = ''

    def desc(self):
        return f'Nome: {self.nome}, Idade: {self.idade} anos, Espécie: {self.especie}'