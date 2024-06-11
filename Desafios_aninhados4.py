#DESAFIO 01

#Escreva um programa para aprovar um empréstimo bancário
#para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai
#pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode
#exceder 30% do salário ou então o empréstimo será negado.
#print ('***************SIMULE SEU EMPRESTIMO**********************')
# valor_casa = float(input('Qual o valor da casa? '))
# salario = float(input('Qual seu salario? '))
# prazo = float(input('Em quantos anos (digite em meses) sera parcelado? '))

# prest= valor_casa/prazo
# max_prest= salario*30/100

# if prest > max_prest:
#     print('Não aprovado')
# else:
#     print('Aprovado')

#DESAFIO 02
#Escreva um programa que leia dois números inteiros e
#compare- os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
#print ('***************COMPARACAO***********************')
# num1 = 1
# num2 = 0

# if num1>num2:
#     print ('O primeiro valor é maior')
# elif num1<num2:
#     print( 'O segundo valor é maior')
# else:
#     print( 'Nao existe valor maior, os dois sao iguais')

#DESAFIO 03
#Crie um programa que leia duas notas entre 0 a 10 de um aluno
#e calcule sua média, mostrando uma mensagem no final, de
#acordo com a média atingida.

#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 a 6.9: RECUPERAÇÃO
#Média igual ou superior a 7.0: APROVADO
#print ('***************SIMULE SUA NOTA***********************')
# resultado_1 = float(input('Qual a sua nota 1? '))
# resultado_2 =float(input('Qual a sua nota 2? '))

# media = (resultado_1 + resultado_2)/2

# if media<5:
#     print('Você foi reprovado!')
# elif media<6.9 or media<=5:
#     print('Esta de recuperacao!')
# else:
#     print('Aprovado!!!')


#DESAFIO 04
#A confederação Nacional de Natação precisa de uma programa 
#que leia o ano de nascimento de uma atleta e mostre sua
#categoria, de acordo com a idade.

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 24 anos: SÊNIOR
#Acima: MASTER
#print ('***************CLASSIFIQUE OS NADADORES**********************')
# from datetime import datetime

# Niver_nadador= int(input('Qual o ano de nascimento? '))
# current_year = datetime.now().year
# idade = current_year-Niver_nadador

# if idade<9:
#     print('MIRIM')
# elif 9<idade<14:
#     print('INFANTIL')
# elif 14<idade<19:
#     print('JUNIOR')
# elif 19<idade<24:
#     print('SENIOR')
# else:
#     print('MASTER')

#DESAFIO 05
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
#de mostrar que tipo de triângulo será formado:

#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes
# print ('***************QUAL TIPO DE TRIANGULO?********************')
# A= float(input('Digite o comprimento da aresta a: '))
# B= float(input('Digite o comprimento da aresta b: '))
# C= float(input('Digite o comprimento da aresta c: '))

# if A+B>C and A+C>B and B+C>A:
#     print('Pode ser triangulo!')
#     if A == B == C:
#         print('Triângulo Equilátero: todos os lados iguais')
#     elif A == B or A == C or B == C:
#         print('Triângulo Isósceles: dois lados iguais')
#     else:
#         print('Triângulo Escaleno: todos os lados diferentes')
# else:
#     print('Não é possível formar um triângulo!')
 



#JOKENPÔ
#print ('***************JOKENPOO!************************')
# mao_1 = int(input('Escolha um numero de 0 a 5: '))

# import random

# numComp = random.randint(0,5)
# print({numComp})

# if numComp > mao_1:
#     print ('O computador ganhou!')
# else:
#     print( 'Você ganhou!')

