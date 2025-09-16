class Aluno:
    def __init__(self):
        self.nome = ''
        self.nota_1 = 0.0
        self.nota_2 = 0.0
        self.media = 0.0
        self.status = ''
    
    def calcula_media(self):
        self.media = (self.nota_1 + self.nota_2) / 2
        if(self.media >= 70):
            self.status = 'Aprovado'
        else:
            self.status = 'Reprovado'