import os
import configparser
from dotenv import load_dotenv
import keyboard


class Main:

# ----- init -----

    def __init__(self):

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        hold_Or_Toggle_Value = self.config['General']['hold_Or_Toggle'].lower()

        self.va_Active = False
        self.activation_Key_Hold = self.config.getboolean(['General']['use_Hold'])
        self.enable_Conv_Log = self.config.getboolean(['General']['enable_Conversation_Logging'])
        self.always_New_Conv = self.config.getboolean(['General']['always_New_Conversation'])
        self.keep_VA_Active = self.config.getboolean(['General']['keep_VA_Active'])
        

        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.activate_VA)
        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.record_Voice)
        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.new_Conversation)
        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.add_Screenshot)
        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.add_Clipboard)
        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.send)
        keyboard.add_hotkey(self.config['Hotkeys']['va_Activation_Key'], self.stop)


# ----- Keyboard Actions -----

    def activate_VA(self):
        self.va_Active = not self.va_Active
        print(self.va_Active)

    def record_Voice(self):
        pass

    def new_Conversation(self):
        pass

    def add_Screenshot(self):
        pass

    def add_Clipboard(self):
        pass

    def send(self):
        pass

    def stop(self):
        pass


# ----- Main Loop -----

    def main_Loop(self):
         keyboard.wait()


# ------

if __name__ == '__main__':
    VA = Main()
    VA.main_Loop()