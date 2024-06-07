# #Desafio 01 Crie um programa que leia o nome completo de uma pessoas e mostre:
# # #O nome com todas as letras maiúsculas
# nome1= input('Digite seu nome inteiro: ')
# # print(f' O nome inserido foi: {nome1.upper()}')

# #O nome com todas as letras minúsculas
# print(f' O nome inserido foi: {nome1.lower()}')

# #Quantas letras ao todo (sem considerar espaços)
# # nome1_semEspaco= nome1.replace(" ", "")
# print(f' O nome inserido tem: {len(nome1_semEspaco)} letras')

# #Quantas letras tem o primeiro nome
# primeiroNome= nome1.split()
# print(primeiroNome)
# print(f' Seu primeiro nome tem: {len(primeiroNome[0])} letras')

# Desafio 02: Crie um programa que leia o nome de uma cidade e siga se ela 
# # começa ou não com o nome “Santo”.

#city = input('Digite o nome da sua cidade: ')
#city_1 = city.split()
#city_1Maiusc = city_1[0].upper() -Melhor jeito de impedir que diferenças de caixa alta e baixa retornem valor falso, assim transformo tudo em caixa alta e na hora de procurar procuro como caixa alta tambem
#verificanome = "SANTO" in city_1Maiusc
#print(f"A sua cidade {city} começa com santo? {verificanome}")
      
#DESAFIO 03 Crie um programa que leia o nome de uma pessoa e diga se 
# # ela tem "Silva" no nome

# nome2 = input('Qual o seu nome? ')
# print(f" O seu nome tem SILVA? {('Silva' in nome2)}")

# #DESAFIO 04: Faça um programa que leia uma frase pelo teclado e mostre:
# frase= input('Digite qualquer frase que não contenha numeros:')
# #Quantas vezes aparece a letra "A"
# print(f"A sua frase tem {frase.count('a')} letras a")
# #Em que posição ela aparece a primeira vez
# print(f"A letra aparece a primeira vez na posicao {frase.find('a')}")
# #Em que posição ela aparece a ultima vez
# print(f"A letra A aparece a última vez na posicao {frase.rfind('a')}") - CORRIGIR! Rfind?

#DESAFIO 05: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o ultimo nome separadamente

# nomeQuerido = input('Qual seu nome querido?')
# nome_separado = (nomeQuerido.split())
# print(f"Primeiro nome: {nome_separado [0]}")
# print(f"Segundo nome: {nome_separado [1]}")

#Desafio 5
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#Exemplo: Ana Maria De Souza
#Primeiro: Ana
#Ultimo: Souza

#nomeCompleto = str(input("Digite seu nome: "))

#divideNome = nomeCompleto.split() #Inicia cada palavra dentro de um array
#tamanhoArray = len(divideNome)
#inicioNome = divideNome[0]
#fimNome = divideNome[tamanhoArray - 1]

#print(f"Primeiro Nome: {inicioNome}")
#print(f"Ultimo Nome: {fimNome}")


