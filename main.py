import datetime
import re
import threading
import tkinter as ttk
from time import sleep
from tkinter import *

import pyglet


class Application:
    def __init__(self):
        self.hour = None
        self.minute = None

        self.start = False

        self.root = self._getWindow("Будильник")

        self.entry = ttk.Entry()
        self.entry.pack(anchor=NW, padx=6, pady=6)

        self.entry_val = None
        self.label_val = None

        self.label = ttk.Label(text="Формат HH:MM")
        self.label.pack(anchor=NW, padx=6, pady=6)


    def _checkString(self, s):
        if re.match('^[0-2][0-3]:[0-5][0-9]$', s) is not None:
            return True
        else:
            return False

    def _isTimeToRing(self, hour, minute):
        time_now = datetime.datetime.now()
        return (time_now.hour == hour and time_now.minute == minute)

    def _getWindow(self, name="Window", size=(250,100)):
        sizeStr = "{}x{}".format(size[0], size[1])

        root = Tk()
        root.title(name)
        root.geometry(sizeStr)

        return root

    def show_message_wrapper(self):
        self.entry_val = self.entry.get()
        self.show_message()

    def show_message(self):
        if (self._checkString(self.entry_val)):
            
            self.label_val = "Будильник установлен на: " + self.entry_val
            self.label["text"] = self.label_val
            s = self.entry_val

            sh = str(s[0]+s[1])
            sm = str(s[3]+s[4])
            self.hour = int(sh)
            self.minute = int(sm)
            self.music = pyglet.media.load("music.mp3")

            def thread_function():
                while not self._isTimeToRing(self.hour, self.minute):
                    sleep(1)
                    
                self.music.play()

            x = threading.Thread(target=thread_function)
            x.start()

        else: 
            self.label_val = "Некорректный ввод данных"
            self.label["text"] = self.label_val

    def run(self):
        btn = ttk.Button(text="Установить", command=self.show_message_wrapper)
        btn.pack(anchor=NW, padx=6, pady=6)

        self.root.mainloop()
