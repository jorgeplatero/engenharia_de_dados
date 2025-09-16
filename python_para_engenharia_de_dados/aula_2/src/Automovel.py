class Automovel:
   
    def __init__(self):
        self.ano = 0
        self.modelo = ''
        self.chassi = ''
        self.marca = ''
        self.cor = ''
        self.placa = ''
 
    def ligar(self):
        print('Carro ligando ....')
 
    def desligar(self):
        print('Carro desligando ....')
 
    def acelerar(self):
        print('Carro acelerando ....')
 
    def frear(self):
        print('Carro freiando ....')  
 
    def travar_portas(self):
        print('Portas Travadas ....')    
 
    def imprimir(self):
        print('Marca ....: ', self.marca)
        print('Modelo ...: ', self.modelo)
        print('Ano ......: ', self.ano)
        print('Cor ......: ', self.cor)
        print('Chassi ...: ', self.chassi)
        print('Chassi ...: ', self.placa)