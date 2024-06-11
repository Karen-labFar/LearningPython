# #DESAFIO 01 Escreva um programa que faça o computador “pensar” em um número inteiro entre 5 e 0 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# # O programa deverá escrever na tela se o usuário venceu ou perdeu.
# print ('***************JOGO ADIVINHE*************************')
# import random

# print("*********Jogo do adivinhe o numero*************")
# jogoNum= int(input('Digite um numero inteiro de 0 a 5: '))

# numComp = random.randint(0,5)
# print(numComp)

# if jogoNum == numComp:
#     print('Voce acertou, parabens!:)')
# else:
#     print('Voce perdeu! Tente outra vez :(')

# input ()
    
#DESAFIO 02 Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.

#print ('***************CALCULO MULTA*************************')

# deOlhona_Multa = float(input('A que velocidade o carro estava (Km/h)? '))
# valor_multa = float(deOlhona_Multa - 80) * 7
# if deOlhona_Multa >80:
#     print(f'Deu ruim colega! Voce tera que pagar uma multa no valor de {valor_multa} reais, com vencimento 30 dias apos o ocorrido')
# else:
#     print('Ta tudo certo, zero multa')


#DESAFIO 03 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas.
# print ('***************CALCULE DE VIAGEM************************')
# distancia_trip = float(input('Qual a distancia da sua viagem (Km/h)? '))

# if distancia_trip <=200:
#     valor_passagem= distancia_trip * 0.5
#     print(f'O valor da sua passagem sera de {valor_passagem} reais')
# else:
#     valor_passagem_longa= distancia_trip * 0.45
#     print(f'O valor da sua passagem sera de {valor_passagem_longa} reais')
    
# #DESAFIO 04 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#print ('***************ORDENANOD NUMEROS***********************')
# num1 = float(input('Digite um numero:'))
# num2 = float(input('Digite outro numero:'))
# num3 = float(input('Digite mais um numero:'))

# cond1 = num1>num2 and num1>num3
# cond2 = num2>num1 and num2>num3
# cond3 = num1<num2 and num1<num3
# cond4 = num2<num1 and num2<num3


# if cond1:
#     print('O primeiro é maior')
# elif cond2:
#     print('O segundo é maior')
# else:
#     print('O terceiro é maior')

# if cond3:
#     print('O primeiro é o menor')
# elif con4:
#     print('O segundo é o menor')
# else:
#     print('O terceiro é o menor')
    
#EXEMPLO - média de escola
#Aprovado acima de 6 e rerovado abaixo de 3

# media =2
# if media>6:
#     print('Aprovado!')
# else:
#     if media<3:
#         print('Reprovado!')
#     else:
#         print('Recuperacao')

# media =7
# if media>6:
#      print('Aprovado!')
# elif media<3:
#     print('Reprovado!')
# else:
#     print('Recuperacao')
        
    

#Aprovado se media maior ou igual a 7, mas tambem não pode ter mais de 10 faltas
# print ('***************APROVADO OU NAO?**********************')
# notafinal = float(input('Digite a nota do aluno: '))
# faltas = int(input('Quantas faltas o aluno tem? '))

# if notafinal >=7 and faltas<10:
#     print('Voce foi aprovado1')
# elif notafinal >5 and notafinal<7 and faltas<10:
#     print('Voce esta de recuperacao!')
# else:
#     print('Voce reprovou!')
    



#DESAFIO 05 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#print ('***************PODE SER TRIANGULO?***********************')
# #Condições Necessárias: a + b > c; a + c > b; b + c > a

# A= float(input('Digite o comprimento da aresta a: '))
# B= float(input('Digite o comprimento da aresta b: '))
# C= float(input('Digite o comprimento da aresta c: '))

# if A+B>C and A+C>B and B+C>A:
#     print('Pode ser triangulo!')
# else:
#     print ('Não é possivel formar um triangulo!')
    