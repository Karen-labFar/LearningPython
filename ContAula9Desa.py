# DESAFIO 06
# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os
# valores pares e impares e ordem crescente.
# valores = [[],[]]

# for val in range (7):
#     val= int(input(f'Digite o {val+1}° numero: '))

#     if val%2 ==0:
#         valores[0].append(val)
#     else:
#         valores[1].append(val)

# valores.sort()
# valores[0].sort()
# valores[1].sort()
# print(f' Esses são os impares{valores[1]}')
# print(f'Esses são os pares {valores[0]}')
# print(f'EM ordem crescente {valores}')


# DESAFIO 07
# Crie um programa que cria uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.
# No final mostre a Matriz na tela, com a formatação correta.

# matriz = [[0,0,0],[0,0,0],[0,0,0]] #Cada lista é uma linha

# for linha in range (3):
#     for coluna in range (3):
#      matriz[linha][coluna] =int(input(f'Digite um valor para a posição [{linha},{coluna}]: '))
# print('Matriz 3x3:')
# for linha in matriz:
#     for elemento in linha:
#         print(f'{elemento:^5}', end=' ')
#     print()

# DESAFIO 08
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]] #Cada lista é uma linha

for linha in range (3):
    for coluna in range (3):
        matriz[linha][coluna] =int(input(f'Digite um valor para a posição [{linha},{coluna}]: '))

print('Matriz 3x3:')
for linha in matriz:
    for elemento in linha:
        print(f'{elemento:^5}', end=' ')
    print()
pares= []
impares=[]
matriz_linhadois = matriz[1]

for linha in matriz: #Para cada lista dentro da matriz
    for i in linha: #Para cada item dentor de cada linha da matriz
        if i%2==0:
         pares.append(i)
        else:
         impares.append(i)

print(f' A soma dos numeros pares da matriz é: {sum(pares)}')
print(f' A soma dos numeros impares da matriz é: {sum(impares)}')
print(f' O maior numero da segunda linha da matriz é: {max(matriz_linhadois)}')

