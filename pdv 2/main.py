import pygetwindow
import sys


from module.telegram import TelegramBot
from module.config import Config

from module.screen import *


def main(config_file):
    try:
        Config.load_config(config_file)
        TelegramBot.load_config()

        pesquisar()
        
        if len(pygetwindow.getWindowsWithTitle('NFC-e')) != 0:
            windows = pygetwindow.getWindowsWithTitle('NFC-e')
        else:
            windows = pygetwindow.getWindowsWithTitle('DBVendaPDV')

        fechamento_caixa()
        digita_senha()
        imprimir_fechamento()
        sair()
        
        TelegramBot.send_message(mensagem)


        exit()
    except Exception:
        print("😬 Ohh no! We couldn't start the bot.")

if __name__ == "__main__":
    config_path = "config.yaml"

    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        config_path = f"config_profiles/{config_file}.yaml"

    main(config_path)

