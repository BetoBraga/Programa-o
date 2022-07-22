from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import openpyxl

#README - O código a seguir necessita do webdriver Edge.
#Autor - Roberto Márcio Braga Junior

# Load planilhas
# Abre Planilha de Read-Referencias
planread = openpyxl.load_workbook('steal1.xlsx')
sheet = planread.active
# Abre Planilha de Write-Detalhes
planwrite = openpyxl.load_workbook('steal2.xlsx')
sheetw = planwrite.active

# Abre o Navegador
driver = webdriver.Edge('D:\OneDrive\Documents\SPOT\scrp\msedgedriver.exe')

# Realiza Login no Fornecedor
driver.get("hwww.sitedofornecedor.como")
driver.find_element(By.NAME, "login").send_keys("usuario")
driver.find_element(By.NAME, "pwd").send_keys("senhadousuario" + Keys.ENTER)

# Inicia o loop
contador = 1
while (contador < 2):
    contador2 = "A"
    # Seleciona a célula do contador secundário + o contador de linhas.
    s = f'{contador2}{contador}'
    # Atribui a variável re o valor da celula atual.
    re = sheet[s].value
    re = "{}".format(re)

    # Seleciona a barra de pesquisar
    driver.find_element(By.ID, "input-search").send_keys(re + Keys.ENTER)
    elemento = driver.find_element(By.TAG_NAME, 'div.ref')
    elemento = "{}".format(elemento)
    sheetw[s].value = elemento
    

	# Proximo item...
    #contador2 = "B"
    #s = f'{contador2}{contador}'

    planwrite.save('steal2.xlsx')
    contador2 = "A"
    contador += 1
    print(contador)
    print(contador2)



