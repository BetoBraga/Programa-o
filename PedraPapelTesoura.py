import random
import os
import time

os.system("clear")
condicao = True
campeaosupp = 1


while condicao == True:

    print("Bem vindo ao Pedra, Papel, Tesoura.")
    print("***********************************")
    print("Selecione a opção digitando o número ao lado.")
    print("***********************************")
    print("1 - Pedra.")
    print("2 - Papel.")
    print("3 - Tesoura.")

    opcao = int(input("Qual você escolhe? - "))

    os.system("clear")
    print("Aguarde enquanto o computador escolhe...")
    time.sleep(5)
    os.system("clear")

    comp = random.randint(1,3)

    if opcao == 1:
        opcao_str = "Pedra"
    elif opcao == 2:
        opcao_str = "Papel" 
    elif opcao == 3:
        opcao_str = "Tesoura"
        
    if comp == 1:
        comp_str = "Pedra"
    elif comp == 2:
        comp_str = "Papel" 
    elif comp == 3:
        comp_str = "Tesoura"  

    if opcao == comp:
        print("Houve um empate! Ambos escolheram ", opcao_str)
        campeaosupp = 2
        campeao = None
    elif opcao == 1 and comp == 3:
        campeao = True
    elif opcao == 1 and comp == 2:
        campeao = False
    elif opcao == 2 and comp == 1:
        campeao = True
    elif opcao == 2 and comp == 3:
        campeao = False
    elif opcao == 3 and comp == 2:
        campeao = True
    elif opcao == 3 and comp == 1:
        campeao = False
        
    print("Você escolheu " + opcao_str + " e o computador escolheu " + comp_str)

    if campeao is True:
        print("Logo, você venceu!")
    elif campeao is False:
        print("Infelizmente, você perdeu. :( Mais sorte da próxima vez.")
    elif campeaosupp == 2:
        print("A máquina é trapaceira! Hahaha! - Disse o Computador.")
    
    condicao = int(input("Deseja jogar novamente? - 1 para Jogar Novamente / 0 para sair: "))
    os.system("clear")
    if condicao == 0:
        print("Adeus! :(")
        time.sleep(2)
        exit()
        condicao = False
