import os
os.system("clear")

condicao = 1
while condicao == 1:
    print("Bem-vindo ao conversor de temperatura! ")

    print("1 - Kelvin")
    print("2 - Fahrenheit")
    print("3 - Celsius")

    opcao = int(input("Selecione a primeira escala: "))

    print("1 - Kelvin")
    print("2 - Fahrenheit")
    print("3 - Celsius")

    opcao2 = int(input("Selecione a segunda escala: "))

    if opcao == 1:
        opcao_nome = "Kº"
    elif opcao == 2:
        opcao_nome = "Fº"
    elif opcao == 3:
        opcao_nome = "Cº"
            
    temp_i = int(input("Insira a temperatura em " + opcao_nome + ": "))
            
    if opcao2 == 1:
        opcao_nome2 = "Kº"
    elif opcao2 == 2:
        opcao_nome2 = "Fº"
    elif opcao2 == 3:
        opcao_nome2 = "Cº"
            
    if opcao == 1:
        if opcao2 == 1: #Kelvin - Kelvin 
            temp_f = temp_i
            temp_f = round(temp_f, 2)
        elif opcao2 == 2: #Kelvin - Fahrenheit
            temp_f = (temp_i - 273.15) * 9/5 + 32
            temp_f = round(temp_f, 2)
        elif opcao2 == 3: #Kelvin - Celsius
            temp_f = temp_i - 273.15
            temp_f = round(temp_f, 2)
            
    elif opcao == 2:
        if opcao2 == 1: #Fahrenheit - Kelvin 
            temp_f = (temp_i - 32) * 5/9 + 273.15
            temp_f = round(temp_f, 2)
        elif opcao2 == 2: #Fahrenheit - Fahrenheit
            temp_f = temp_i
            temp_f = round(temp_f, 2)
        elif opcao2 == 3: #Fahrenheit - Celsius
            temp_f = (temp_i - 32) * 5/9
            temp_f = round(temp_f, 2)

    elif opcao == 3:
        if opcao2 == 1: #Celsius - Kelvin 
            temp_f = temp_i + 273.15
            temp_f = round(temp_f, 2)
        elif opcao2 == 2: #Celsius - Fahrenheit
            temp_f = (temp_i * 9/5) + 32
            temp_f = round(temp_f, 2)
        elif opcao2 == 3: #Celsius - Celsius
            temp_f = temp_i
            temp_f = round(temp_f, 2)
            
        
    print(f'{temp_i}{opcao_nome} são {temp_f}{opcao_nome2}')
    condicao = int(input("Deseja realizar uma nova conversão? 1 para Converter Novamente - 0 para Sair"))
            
        


