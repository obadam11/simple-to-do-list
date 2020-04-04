import tkinter as tk
import datetime


yellow = "#F7FF45"
dark_yellow = "#AFB438"

class App(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = "root"

    def draw(self, title, color="#FFFFFF"):
        # global root
        self.screen = tk.Tk()
        self.screen.geometry(f"{self.width}x{self.height}")
        self.screen.config(bg=color)
        self.screen.title(title)
    
    def stay_running(self):
        self.screen.mainloop()
    
    def entry_bar(self, x, y, width=180):
        eb = tk.Entry(self.screen, borderwidth=5)
        eb.place(x=x, y=y, width=width)
    
    def but(self, background, x, y, width ,text):
        button = tk.Button(self.screen, text=text, bg=background, font=("Corier", 10, "bold"), borderwidth=5)
        button.place(x=x, y=y, width=width)
    
    def list_box(self, x, y, width, height):
        lb = tk.Listbox(self.screen)
        lb.place(x=x, y=y, width=width, height=height)
    
    def on_screen(self, x, y, txt, background, foreground="black"):
        t = tk.Label(self.screen, text=txt, bg=background, fg=foreground)
        t.place(x=x, y=y)



