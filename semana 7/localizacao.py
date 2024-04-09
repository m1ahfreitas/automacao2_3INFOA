import pyautogui
#localizar x, y de uma imagem na tela
nome_XY = pyautogui.locateCenterOnScreen('./semana 7/capo_nome.png')
pyautogui.click(nome_XY, duration=0.5)#clica
pyautogui.write('Maiara Freitas')

cpf_XY = pyautogui.locateCenterOnScreen('./semana 7/campo_cpf.png')
pyautogui.click(cpf_XY, duration=0.5)#clica
pyautogui.write('138.620.996-10')

email = pyautogui.locateCenterOnScreen('./semana 7/email.png')
pyautogui.click(email, duration=0.5)#clica


sim = pyautogui.locateCenterOnScreen('./semana 7/sim.png')
pyautogui.click(sim, duration=0.5)#clica
