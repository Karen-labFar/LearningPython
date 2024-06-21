# DESAFIO 01
# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.
# print('_________DESAFIO 01 DAS LISTAS AULA 08______________')
# valores = []

# for val in range (0,5):
#     val= int(input(f'Digite o {i+1}° numero: '))
#     valores.append(val)
# print(valores)
#if i==0:
# maior = menor= numero
#else:
#if numero> maior:
# maior=numero
#if numero<menor:
# menor=numero
# print(f' O maior valor digitado foi: {max(valores)} e ele esta na posição {valores.index(max(valores))}')
# print(f' O menor valor digitado foi: {min(valores)} e ele esta na posição {valores.index(min(valores))}')
# print('____________________FIM______________________')


# DESAFIO 02
# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente.
# print('_________DESAFIO 02 DAS LISTAS AULA 08______________')
# nova = []

# while True:
#     num= int(input('Digite um numero inteiro (0 para sair):'))
#     if num==0:
#         break
#     if num in nova:
#         print('Este valor ja esta na lista')
#     else:
#         nova.append(num)
# nova.sort()
# print(nova)

# print('____________________FIM______________________')

# DESAFIO 03
# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada na tela
# print('_________DESAFIO 03 DAS LISTAS AULA 08______________')
# valores = []

# for val in range (5):
#     val= int(input(f'Digite o {val+1}° numero: '))
    
#     if len(valores) == 0 or val > valores[-1]: #Se a lista estiver vazia ou o valor inserido 
#     #for maior que o último valor da lista, o valor é adicionado ao final.
#         valores.append(val)
#     else: #Caso contrário, o código percorre a lista para encontrar a posição correta para o novo valor, 
# #inserindo-o de forma que a lista permaneça ordenada.
#         pos = 0
#         while pos < len(valores): # Loop para percorrer a lista enquanto pos for menor que o tamanho da lista
#             if val <= valores[pos]: #Verifica se o valor a ser inserido é menor ou igual ao valor na posição pos da lista.
#                 valores.insert(pos, val)
#                 break
#             pos += 1

# # Exibindo a lista ordenada
# print(valores)
# print('Lista ordenada:', valores)
# print('____________________FIM______________________')

# DESAFIO 04
# Crie um programa que vai ler vários números e colocar em
# uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
# print('_________DESAFIO 04 DAS LISTAS AULA 08______________')
# lista= []
# pares = []
# impares = []

# while True:
#     num= int(input('Digite um numero inteiro (0 para sair):'))
#     if num==0:
#         break
#     lista.append(num)

# for i in lista:
#     if i %2==0:
#         pares.append(i)
#     else:
#         impares.append(i)
# print(f' os numeros escolhidos foram: {lista}')
# print(f' Os pares são: {pares}')
# print(f' Os impares são: {impares}')

# print('____________________FIM______________________')

# DESAFIO 05
# Faça um programa que leia nome e peso de varias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Um listagem com as pessoas mais leves
# print('_________DESAFIO 05 DAS LISTAS AULA 08______________')
# nome =[]
# peso=[]

# while True:
#     id_usuario= (input('Digite o nome da pessoa:')),int(input('Digite o peso da pessoa:'))
#     inserir= int(input('Caso deseje sair digite 1, para adicionar mais pessoas digite qualquer numero: '))
#     nome.append(id_usuario[0])
#     peso.append(id_usuario[1])
#     if inserir ==1:
#         break
#     else:
#         continue
# leves= []
# pesados=[]
# print(nome)
# print(peso)
# print(len(nome))
# media_pesos = sum(peso)/len(peso)
# print(round(media_pesos,2))

# for i in range(len(nome)):
#     if peso[i] > media_pesos:
#         pesados.append((nome[i]))
#     else:
#         leves.append((nome[i]))

# # Exibindo os resultados
# print(f'Nomes das pessoas: {nome}')
# print(f'Pesos das pessoas: {peso}')
# print(f'Total de pessoas: {len(nome)}')

# print(f'As pessoas leves da lista são: {leves}')
# print(f'As pessoas pesadas da lista são: {pesados}')

# print('____________________FIM______________________')
