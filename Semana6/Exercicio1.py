#exercicio clicar no google para clicar na barra de pesquisa e pesquisar depois dar enter
import pyautogui

pyautogui.click(521, 406, button='LEFT')
pyautogui.write('como automatizar o whatsapp', interval=0.3)
pyautogui.press('enter')

pyautogui.moveTo(32,404, duration= 0.2)
pyautogui.dragTo(505,573, duration= 0.2)
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(1059,521, duration=0.2)
pyautogui.hotkey('ctrl','v')