import os
import pyshorteners

os.system("Clear")
condicao = 1
while condicao == 1:
    url_primitiva = input("Digite a URL que deseja encurtar: ")
    encurtador = pyshorteners.Shortener()
    url_encurtada = encurtador.tinyurl.short(url_primitiva)
    print("Parabéns! Sua URL foi encurtada!")
    print("Sua nova URL é " + url_encurtada)
    condicao = int(input("Deseja encurtar outra URL? 1 para Encurtar Novamente - 0 para Sair"))
                
            
