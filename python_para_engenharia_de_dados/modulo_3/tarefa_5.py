import random
from faker import Faker
#from Aluno import Aluno


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



faker = Faker(locale='pt-BR')

nome_arquivo_1 = 'alunos_aprovados.txt'
nome_arquivo_2 = 'alunos_reprovados.txt'

arquivo_1 = open(nome_arquivo_1, 'w')
arquivo_2 = open(nome_arquivo_2, 'w')

lista_alunos_aprovados = []
lista_alunos_reprovados = []

for x in range(20):
    a = Aluno()
    a.nome = faker.name()
    a.nota_1 = random.randint(30, 100)
    a.nota_2 = random.randint(30, 100)
    a.calcula_media()
    if a.media >= 70:
        lista_alunos_aprovados.append(a)
    else:
        lista_alunos_reprovados.append(a)


arquivo_1.write('nome' + ';' + 'nota_1' + ';' + 'nota_2' + ';' + 'media' + ';' + 'status' + '\n')
for aluno in lista_alunos_aprovados:
    arquivo_1.write(aluno.nome + ';' + str(aluno.nota_1) + ';' + str(aluno.nota_2) + ';' + str(aluno.media) + ';' + aluno.status + '\n')
arquivo_1.close()

arquivo_2.write('nome' + ';' + 'nota_1' + ';' + 'nota_2' + ';' + 'media' + ';' + 'status' + '\n')
for aluno in lista_alunos_reprovados:
    arquivo_2.write(aluno.nome + ';' + str(aluno.nota_1) + ';' + str(aluno.nota_2) + ';' + str(aluno.media) + ';' + aluno.status + '\n')
arquivo_2.close()