from AnimalEspecie import Gato, Cachorro, Coelho


print('--- Criando um gato ---')
gato = Gato()
gato.nome = 'Mia'
gato.idade = 3
gato.cor_pelo = 'Branco'
gato.raca = 'Siamês'
print(gato.desc())
print(f'Som do gato: {gato.emitir_som()}')
print(f'Cor do pelo: {gato.cor_pelo}')
print(f'Raça do gato: {gato.raca}\n')

print('--- Criando um cachorro ---')
cachorro = Cachorro()
cachorro.nome = 'Bob'
cachorro.idade = 5
cachorro.porte = 'Grande'
cachorro.raca = 'Pastor Alemão'
print(cachorro.descricao())
print(f'Som do cachorro: {cachorro.emitir_som()}')
print(f'Porte do cachorro: {cachorro.porte}')
print(f'Raça do cachorro: {cachorro.raca}\n')

print('--- Criando um coelho ---')
coelho = Coelho()
coelho.nome = 'Pernalonga'
coelho.idade = 3
coelho.cor_pelo = 'Cinza'

print(coelho.desc())
print(f'Som do coelho: {coelho.emitir_som()}')
print(f'Cor do pelo: {coelho.cor_pelo}')