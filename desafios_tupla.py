# DESAFIO 01

# Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostra-lo por extenso.
# contagem= ('ZERO', 'UM', 'DOIS', 'TRES','QUATRO', 'CINCO')
# inser_num = int(input('Digite um numero de 0 a 5: '))
# print(f"Você digitou: {contagem[inser_num]}.")

# DESAFIO 02

# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla.
# Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na Tupla.
#Op 1
# maior=0
# menor=0
# minhalista=[]

# for i in range(1,6):
#     numeroaleatorio= random.randint(1,5)
#     minhalista.append(numeroaleatorio)
# print(minhalista)

# maior = max(minhalista).....
#Op2
# minhatupla = (randint(1,10), randnit(1,10).....)
# for numeros in minhatupla:
#     print(f'{numeros}', end=' ')

# import random
# num_aleatorio = []
# while len(num_aleatorio)<5:
#     ranlista= random.randint(0,10)
#     num_aleatorio.append(ranlista)
# num_aleatorio_tu = tuple(num_aleatorio)
# print(num_aleatorio_tu)
# print(f' O maior número é {max(num_aleatorio_tu)}')
# print(f' o menor número é {min(num_aleatorio_tu)}')

# DESAFIO 03

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro Serie B de Futebol, na ordem de
# colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.

# B) Os últimos 4 colocados da tabela.

# C) Uma lista com os times em ordem alfabética.

# D) Em que posição na tabela está o time do Santos.

# times = ('SP', 'FLAMENGO', 'CORINTHIANS', 'PALMEIRAS','VASCO', 'SANTOS')
# print(f' Os cinco primeiro colocados são: {times[:5]}')
# print(f'Os quatro último colocados são: {times[-4:]}')
# print(f' Em ordem alfabetica, os times ficam : {sorted(times)}')
# print(f" O Santos está em: {times.index('SANTOS')+1} lugar")


# DESAFIO 04

# Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram o números pares.


# valor_tupla = int(input('Digite um numero:')),int(input('Digite um numero:')), int(input('Digite um numero:')), (int(input('Digite um numero:')))
# print(valor_tupla)
# print(f'O numero 9 aparece : {valor_tupla.count(9)} vez')
# if 3 in valor_tupla:
#     print(f'O numero 3 aparece a primeira vez na posicao: {valor_tupla.index(3)}')
# par=[]
# for i in valor_tupla:
#     if i%2==0:
#         par.append(i)
# print(f' Os numeros pares são {par}')
    
# DESAFIO 05

# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em
# forma tabular.

produtos_price= (
    'Shampoo', 16.0,
    'Sabonete', 4.0,
    'Listerine', 20.0,
    'Pasta de dente', 4.0
)
print('_'*30)
print(f'{'Lista de preços':^30}')
print('-'*30)

for i in range(0, len(produtos_price),2):
    produto = produtos_price[i]
    preco = produtos_price[i+1]
    print(f'{produto:<20} R$ {preco: >5.2f}') #formatação {:<20} e {:>5.2f} é usada para alinhar os nomes dos produtos à esquerda e os preços à direita, com duas casas decimais.
print('_'*30)
    
    
#     #Desafio 4
# numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),\
#             int(input('Digite um número: ')),int(input('Digite um número: ')))

# #Quantas vezes o "9" aparece
# print(f"O valor 9 apareceu {numeros.count(9)} vezes")

# ##Mostra a posição do "3" se ele existir
# if 3 in numeros:
#     print(f"O valor 3 esta na {numeros.index(3)+1}° posicao")
# else:
#     print(f"O valor 3 não aparece nessa tupla")

# print(f"Os valores pares são ", end='')

# ##Imprime apenas os Pares da Tupla
# for n in numeros:
#     if n % 2 == 0:    
#         print(n, end=' ')