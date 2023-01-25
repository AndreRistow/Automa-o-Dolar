#Automação para conferir valor do dolar e repassar informação via e-mail
import pyautogui
import time


pyautogui.PAUSE = 1
#Abrir navegador e pesquisar por valor do dolar
time.sleep(2)
pyautogui.press(["Win"])
pyautogui.write("Chorme")
pyautogui.press(["enter"])
time.sleep(2)
pyautogui.write("google")
time.sleep(2)
pyautogui.press(["enter"])
pyautogui.write("cotacao do dolar")
pyautogui.press(["enter"])
pyautogui.click(1117,372, duration=0.5)
pyautogui.dragTo(808,370,2, button="left")

pyautogui.keyDown("Ctrl")
pyautogui.press(["c"])
pyautogui.keyUp("Crtl")

#Abrir aba anonima para executar email
pyautogui.hotkey("Ctrl","Shift","n")
pyautogui.write("gmail.com")
pyautogui.press(["enter"])
time.sleep(3)
pyautogui.write("email**")
pyautogui.press(["enter"])
time.sleep(2)
pyautogui.write("senha**")
pyautogui.press(["enter"])
time.sleep(5)
pyautogui.click(1312,41, duration=0.5)
pyautogui.click(63,208, duration=0.5)
time.sleep(1)
pyautogui.write("email**")
pyautogui.press(["enter"])
pyautogui.press(["tab"])
pyautogui.write("Cotacao do dolar")
pyautogui.press(["tab"])
pyautogui.keyDown("Ctrl")
pyautogui.press(["v"])
pyautogui.keyUp("Ctrl")
time.sleep(1)
pyautogui.click(833,697, duration=0.5)

#Fechar aba anonima do email
time.sleep(2)
pyautogui.keyDown("Alt")
pyautogui.press(["F4"])
pyautogui.keyUp("Alt")
pyautogui.press(["enter"])
pyautogui.keyDown("Alt")
#Fim