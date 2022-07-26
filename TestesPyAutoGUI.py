

import pyperclip
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() # setar padrão tela
screenWidth, screenHeight
(2560, 1440)

currentMouseX, currentMouseY = pyautogui.position() # setar padrão mouse
currentMouseX, currentMouseY
(1314, 345)






#load excel referencias
pyautogui.click(165,755)
time.sleep(3)

pyautogui.click(751,154)
time.sleep(3)

pyautogui.write('D:\OneDrive\Documents\****')
pyautogui.press('enter')

pyautogui.doubleClick(436,263)
time.sleep(3)

#verify first
pyautogui.keyDown('ctrl')
pyautogui.press('up')
pyautogui.keyUp('ctrl')

pyautogui.keyDown('ctrl')
pyautogui.press('left', presses= 5)
pyautogui.keyUp('ctrl')

pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

codigo = pyperclip.paste()


#buscar infos

pyautogui.click(122,749)
pyautogui.PAUSE = 1
 

pyautogui.click(348,51)
pyautogui.PAUSE = 1

pyautogui.write('www.*****.com.br/pt/')
pyautogui.press('enter')

pyautogui.moveTo(706,140)
pyautogui.click()
pyautogui.PAUSE = 3
time.sleep(3)

pyautogui.click(432,140) 

pyautogui.write(codigo)
pyautogui.press('enter')

# copy
pyautogui.moveTo(638,362)
pyautogui.click(clicks=3)

pyautogui.keyDown('ctrl')
pyautogui.press('c')
pyautogui.keyUp('ctrl')

copyref = pyperclip.paste()
