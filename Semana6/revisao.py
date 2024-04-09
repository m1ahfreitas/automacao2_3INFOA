import pyautogui

#movimentar o mouse utilizando toda a tela
pyautogui.moveTo(960, 540, duration=.5)
#movimentar o mouse relativo aonde o ponteiro está
pyautogui.moveRel(100, 100, duration=.5)


#arrasta o mouse cordenadas absolutas e a outra relativa
pyautogui.dragTo(960,540, duration=.5)
pyautogui.dragRel(960,540, duration=.5)

#clicar absoluto
pyautogui.click(960, 540, clicks=2, button='RIGHT')

#rolagem
pyautogui.scroll(-2)

#teclado

#escrever
pyautogui.write('ola', interval=0.3)

#precionar uma tecla especifica 
pyautogui.press('enter')

#teclas simultaneas
pyautogui.hotkey('crtl', 'a')
pyautogui.hotkey('crtl', 'c')
pyautogui.hotkey('crtl', 'v')

#manter as teclas pressionadas e soltar depois
pyautogui.keyDown('a')
pyautogui.keyUp('a')

