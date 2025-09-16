import random
from faker import Faker
from Aluno import Aluno

faker = Faker(locale='pt-BR')
#nome_arquivo = 'aula_python.txt'
#arquivo = open(nome_arquivo, 'w')
#arquivo.write('Sejam bem-vindos ao curso de Pyhton' + '\n')
#arquivo.write('Turma 9 2025-2')
#arquivo.close()

nome_arquivo = 'alunos.txt'
arquivo = open(nome_arquivo, 'w')
lista_alunos = []
for x in range(20):
    a = Aluno()
    a.nome = faker.name()
    a.nota_1 = random.randint(40, 100)
    a.nota_2 = random.randint(40, 100)
    a.calcula_media()
    lista_alunos.append(a)


arquivo.write('nome' + ';' + 'nota_1' + ';' + 'nota_2' + ';' + 'media' + ';' + 'status' + '\n')
for aluno in lista_alunos:
    arquivo.write(aluno.nome + ';' + str(aluno.nota_1) + ';' + str(aluno.nota_2) + ';' + str(aluno.media) + ';' + aluno.status + '\n')
arquivo.close()