from threading import Timer, Thread, Event
from datetime import datetime
import tkinter as tk

app = tk.Tk()
lab = tk.Label(app, text = "El reloj comenzara en segundos")
lab.pack()

class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def printer():
    tempo = datetime.today()
    clock = "{}:{}:{}".format(tempo.hour, tempo.minute, tempo.second)
    try:
        lab['text'] = clock
    except RuntimeError:
        exit()


t = perpetualTimer(1, printer)
t.start()
app.mainloop()