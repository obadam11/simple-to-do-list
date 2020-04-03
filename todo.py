import tkinter as tk
import datetime

class App(object):

    # root = ""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, title, color="#FFFFFF"):
        global root
        root = tk.Tk()
        root.geometry(f"{self.width}x{self.height}")
        root.config(bg=color)
        root.title(title)
    
    def stay_running(self):
        global root
        root.mainloop()


program = App(500, 500)
program.draw("Obada")
program.stay_running()




