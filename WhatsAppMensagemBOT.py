import pywhatkit
x = 0

# Pywhatkit trabalha com WhatsApp web, neste caso, necessita-se que a máquina tenha um usuário logado.

numeros = ['+5513981126281','+5513981234588','+5513981621378']
if x > 3:
# envia mensagem para números no horário 12:26
    pywhatkit.sendwhatmsg(numeros[x], "Mensagem", 12, 26) # Mensagem mais explicativo
    x += 1
