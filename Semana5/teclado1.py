import pyautogui
#clica no campo do usuário
pyautogui.click(590,477, duration=0.2)
#digita a matricula no campo
pyautogui.write('2022190016', interval=0.5)
#clica no campo senha
pyautogui.click(734, 556,duration=0.2)
#digita a senha
pyautogui.write('Segredo123.')