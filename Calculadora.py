import os
from unittest import result
os.system("clear")

print("Calculadora: ")
print("***********************")
print("1 - Soma")
print("2 - Subtração")
print("3 - Dvisião")
print("4 - Multiplcação")
print("***********************")
escolha = int(input("Selecione a operação: "))

os.system("clear")

x = int(input("Insira o primeiro valor: "))
y = int(input("Insira o segundo valor: "))

def Soma(x, y):
    z = x + y
    return z

def Subtracao(x, y):
    z = x - y
    return z

def Divisao(x, y):
    z = x / y
    return z

def Multiplicacao(x, y):
    z = x * y
    return z

if escolha == 1:
    operacao = "Soma"
    resultado = Soma(x,y)
elif escolha == 2:
    operacao = "Subtração"
    resultado = Subtracao(x, y)
elif escolha == 3:
    operacao = "Divisão"
    resultado = Divisao(x,y)
elif escolha == 4:
    operacao = "Multiplicação"
    resultado = Multiplicacao(x,y)

print(f'O resultado da {operacao} é {resultado}')
