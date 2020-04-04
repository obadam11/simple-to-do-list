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

    def list_box(self, x, y, width, height):
        global lb
        lb = tk.Listbox(self.screen)
        lb.place(x=x, y=y, width=width, height=height)


    def entry_bar(self, x, y, width=180):
        global eb
        eb = tk.Entry(self.screen, borderwidth=5)
        eb.place(x=x, y=y, width=width)
    
    def get_entry(self):
        global eb
        content =  eb.get()
        eb.delete(0, "end")
        return content
    
    def remove_last(self):
        global lb
        lb.delete("end")



    
    def add_to_list_box(self, inserting):
        global lb
        lb.insert("end", inserting)
    

    def but(self, background, x, width ,text, cmd=None, y=85):
        b = tk.Button(self.screen, text=text, bg=background, font=("Corier", 8, "bold"), borderwidth=5, command=cmd)
        b.place(x=x, y=y, width=width)
    

    

    
    def on_screen(self, x, y, txt, background, foreground="black"):
        t = tk.Label(self.screen, text=txt, bg=background, fg=foreground, font=("Courier", 14, "bold"))
        t.place(x=x, y=y)



todo = App(500, 500)
todo.draw("To-Do List", color=yellow)
todo.on_screen(170, 10, "To Do list app", yellow)
todo.entry_bar(160, 50)
todo.list_box(10, 140, 480, 340)

# Add task

def add_task():
    getting = todo.get_entry()
    todo.add_to_list_box(getting)


todo.but(dark_yellow, 160, 75, "Add Task", add_task)

# Remove task

def remove_task():
    todo.remove_last()

todo.but(dark_yellow, 260, 75, "Rmv Task", remove_task)

# Remove all

def remove_all():
    pass

todo.but(dark_yellow, 360, 75, "Rmv all", remove_all)

# order
def order():
    pass

todo.but(dark_yellow, 60, 75, "order", order)




todo.stay_running()
