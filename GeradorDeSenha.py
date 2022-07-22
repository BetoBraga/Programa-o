import random
import os

os.system("clear")

tamanho = int(input("Insira o tamanho da senha (minimo 15): "))

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numeros_f = len(numeros) - 1

simbolos = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "+"]
simbolos_f = len(simbolos) - 1

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letras_f = len(letras) - 1
# 1/3 letras - 1/3 numeros - 1/3 simbolos

tamanho_terco = int(tamanho / 3)

senha_numero = ""
for i in range(0, tamanho_terco):
    x = random.randint(0, numeros_f)
    y = numeros[x]
    senha_numero += y
# VER OS NUMEROS DA SENHA - print(senha_numero)

senha_letra = ""
for i in range(0, tamanho_terco):
    x = random.randint(0, letras_f)
    y = letras[x]
    senha_letra += y
# VER AS LETRAS DA SENHA - print(senha_letra)

senha_simbolo = ""
for i in range(0, tamanho_terco):
    x = random.randint(0, simbolos_f)
    y = simbolos[x]
    senha_simbolo += y
# VER OS SIMBOLOS DA SENHA - print(senha_numero)

#PRINTA UM POR UM print(senha_numero), print(senha_simbolo), print(senha_letra)

senha_final = senha_numero + senha_simbolo + senha_letra

senha_final = ''.join(random.sample(senha_final, len(senha_final)))

#random.shuffle(senha_final)
print("Sua senha deverá ser ", senha_final)
