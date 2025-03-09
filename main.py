import os
import configparser
from dotenv import load_dotenv
import keyboard

config = configparser.ConfigParser()
config.read('config.ini')


def activate_VA():
    print("key pressed")


keyboard.add_hotkey(config['Hotkeys']['va_Activation_Key'], activate_VA)


keyboard.wait()
