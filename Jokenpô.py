
# import random
# while True:
#     op_jogador = int(input("Digite sua escolha: \n1-Pedra \n2-papel  \n3-Tesoura \n digite: "))
# # op_jogador = op_jogador.upper()

#     print(op_jogador)
#     if op_jogador ==1:
#      tx_jogador="PEDRA"
#      img_jogador="🧱"
#     elif op_jogador ==2:
#      tx_jogador="PAPEL"
#      img_jogador ="🧻"
#     elif op_jogador ==3:
#      tx_jogador="TESOURA"
#      img_jogador ="✂"
#     else:
#      print("Opção invalida")

#     print(tx_jogador)
   
#     opcoes =["PEDRA","PAPEL","TESOURA"]
# # numero_randomico = random.randint(0,2) #0 ou 1 ou 2

# # print(opcoes)#random.randint(0,2)
# # print(opcoes[1])#PAPEL
 
# # op_computador= opcoes[numero_randomico]
#     op_computador =random.choice(opcoes)

#     print(f"Esolha jogador: {tx_jogador} - {img_jogador}")
#     print(f"Esolha PC: {op_computador}")

# #VITORIA
#     if (
#         (tx_jogador=="PEDRA" and op_computador=="TESOURA")or
#         (tx_jogador=="TESOURA" and op_computador=="PAPEL")or
#         (tx_jogador=="PAPEL" and op_computador=="PEDRA")    
#     ):
#      print("Você venceu! 😎")
# #Derrota
#     elif (
#         (tx_jogador=="PEDRA" and op_computador=="PAPEL")or
#         (tx_jogador=="TESOURA" and op_computador=="PEDRA")or
#         (tx_jogador=="PAPEL" and op_computador=="TESOURA")    
#     ):
#      print("Você perdeu! 😵")
#     else:
#      print("EMPATE!! 😐")

#     resposta = input('Deseja sair? (s/n): ')
#     if resposta.lower()=="s":
#      print('Saindo')
#      break
# print('')