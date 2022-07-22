import pyautogui
import time
import pyperclip
import openpyxl

# Configuração base
screenWidth, screenHeight = pyautogui.size()
screenWidth, screenHeight
(2560, 1440)
currentMouseX, currentMouseY = pyautogui.position()
currentMouseX, currentMouseY
(1314, 345)

# Loga na XXXX (OBS. Credenciais precisam estar salvas)
pyautogui.click(122, 749)
pyautogui.PAUSE = 3
pyautogui.click(348, 51)
pyautogui.PAUSE = 3
pyautogui.write('www.XXXXXXXXXXX.com.br/')
pyautogui.press('enter')
pyautogui.moveTo(706, 140)
pyautogui.click()
pyautogui.PAUSE = 3
time.sleep(2)

# Abre Planilha de Read-Referencias
planread = openpyxl.load_workbook('teste.xlsx')
sheet = planread.active
# using cell() function

# Abre Planilha de Write-Detalhes
planwrite = openpyxl.load_workbook('testewrite.xlsx')
sheetw = planwrite.active

# Inicia o loop
contador = 1
while (contador < 704):
    # Adiciona a coluna A como contador secundário
    contador2 = "A"
    # Seleciona a célula do contador secundário + o contador de linhas.
    s = f'{contador2}{contador}'
    # Atribui a variável re o valor da celula atual.
    re = sheet[s].value
    # Copia re
    pyperclip.copy(re)
    re = "{}".format(re)

    # Abre o Navegador
    pyautogui.moveTo(560, 144)
    pyautogui.click()

    # Deleta texto pré-existente.
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('del')

    # Escreve o código
    pyautogui.write(re)
    pyautogui.press('enter')
    pyautogui.PAUSE = 3

   
    # Salva o referência do produto copiado na planilha-destino
    pyautogui.moveTo(625, 309)
    pyautogui.click(clicks=3)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    co = pyperclip.paste()
    co = "{}".format(co)

    # Validador
    print(co)
    print(re)
    # Verifica validade da string de entrada na box PESQUISA - caso não corresponda a ref. segue para ELSE
    if re in co:
       sheetw[s].value = co
       # Atualiza coluna (contador secundário) para B
       contador2 = "B"
       s = f'{contador2}{contador}'
       # Salva a descrição do produto copiado na planilha-destino
       pyautogui.moveTo(635, 402)
       pyautogui.click(clicks=3)
       pyautogui.keyDown('ctrl')
       pyautogui.press('c')
       pyautogui.keyUp('ctrl')
       desc = pyperclip.paste()
       desc = "{}".format(desc)
       sheetw[s].value = desc
       # Atualiza coluna (contador secundário) para C
       contador2 = "C"
       s = f'{contador2}{contador}'
       # Salva o nome do produto copiado na planilha-destino
       pyautogui.moveTo(638, 362)
       pyautogui.click(clicks=3)
       pyautogui.keyDown('ctrl')
       pyautogui.press('c')
       pyautogui.keyUp('ctrl')
       nome = pyperclip.paste()
       nome = "{}".format(nome)
       sheetw[s].value = nome
       # Salva a imagem na pasta de download padrão (neste caso, imgs)
       pyautogui.moveTo(240, 647)
       pyautogui.click(button='right')
       pyautogui.moveTo(405, 288)
       pyautogui.PAUSE = 3
       pyautogui.click()
       pyautogui.PAUSE = 3
       pyautogui.press('enter')
       planwrite.save('testewrite.xlsx')
       contador2 = "A"
       contador += 1
       # Segue ao proximo item se não houve resultado referente ao nome  
    else:
       planwrite.save('testewrite.xlsx')
       contador2 = "A"
       contador += 1
      
