
import random
import os
os.system("clear")
condicao = True

while (condicao):
    x = input("Digite o número mínimo: ")
    x_int = int(x)
    y = input("Digite o número máximo: ")
    y_int = int(y)
    z_int = int(0)
    
    
    

    #Gera número secreto e aleatório
    numero = int(random.randrange(x_int, y_int))
    print(numero)
    while (z_int is not numero):
        z = input("Insira um número: ")
        z_int = int(z) 
    else: 
        #Vitória
        os.system("clear")
        escolha = int(input("Parabéns! Você acertou! - 1 para Jogar Novamente / 0 para sair: "))
        os.system("clear")
        if escolha == 0:
            print("Adeus! :(")
            exit()
            condicao = False
            
        
        
        
