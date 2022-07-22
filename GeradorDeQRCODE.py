import qrcode
import os
os.system("clear")

condicao = 1
while condicao == 1:
    print("Bem-vindo ao Gerador de QR Code!")
    print("********************************")
    print("Exemplos de Links:")
    print("mailto:contato@absolemtech.com.br - Direciona o QR Code para uma aba de email vazia com o endereço de envio pré-preenchido")
    print("tel:+5513981126281 - Realiza uma ligação telefonica automaticamente")
    print("www.absolemtech.com.br - Direciona o QR Code ao website selecionado")
    print("********************************")
    link = input("Digite o link ao qual o QR Code deverá ser direcionado: ")
    qr = qrcode.make(link) #Link 
    type(qr)
    nome = input("Como quer salvar o nome do seu arquivo? - ")
    qr.save(nome + ".png")
    print("Salvo com sucesso! Verifique o diretório atual para encontrar seu QR Code!")
    condicao = int(input("Deseja gerar um novo QR Code? 1 para voltar ao início - 0 para Sair"))
            
        
