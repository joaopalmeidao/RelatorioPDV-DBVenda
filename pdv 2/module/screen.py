import pyautogui
import time
from datetime import datetime
import keyring

# password
password = keyring.get_password("dbvenda", "S")

# PDV
pdv = "2"
data = datetime.today().strftime("%d-%m-%Y")
mensagem = "Relatório PDV {} enviado para impressão".format(pdv)

# Parâmetros da tela
size = str(pyautogui.size())
size.split("=")
size_fomatted_x = size[11:15]
size_fomatted_y = size[24:-1]

# if pyautogui.size()==(1920,1080):
#     print(size)

# def config_size(width,height):
#     if width != 1920:

def pesquisar():
    x = 690
    y = 392
    pyautogui.hotkey("win", "r")
    pyautogui.write("C:\DBVenda\Binarios\DBVendaPDV.exe")
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(5)
    pyautogui.press("esc",presses=2)
    time.sleep(1)

def fechamento_caixa():
    pyautogui.click()
    pyautogui.press("f7")
    pyautogui.press("f4")
    time.sleep(2)

def digita_senha():
    pyautogui.write(password)
    pyautogui.press("enter")
    time.sleep(35)

def imprimir_fechamento():
    x = 1115
    y = 648
    pyautogui.screenshot("Vendas PDV-{}--{}.png".format(pdv,data))
    
    time.sleep(1)
    # TelegramBot.send_message_with_image('G:\Meu Drive\pyautogui\relatorio pdv\Vendas PDV--{}.png'.format(data))
    pyautogui.moveTo(x, y)
    pyautogui.click()
    
    time.sleep(1)

def sair():
    x = 1208
    y = 47
    pyautogui.press("esc")
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.press("esc")
    pyautogui.hotkey("alt", "f4")
    pyautogui.press("f1")
    pyautogui.press("f2")
    pyautogui.press("esc", presses=2)
    time.sleep(2)
    pyautogui.press("esc", presses=2)
    pyautogui.press("esc", presses=2)