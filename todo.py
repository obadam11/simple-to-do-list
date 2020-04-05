import tkinter as tk
import datetime
from tkinter import messagebox


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
    
    
    @classmethod
    def get_entry(cls):
        global eb, lb
        content =  eb.get()
        print(content)
        if content:
            eb.delete(0, "end")
            lb.insert("end", content)
        else:
            messagebox.showinfo("Error", "Please enter something")
        try:
            with open("todo.txt", "a") as f_write:
                f_write.write(f"{content}\n")
        except FileNotFoundError:
            print("File not Found")

    @classmethod
    def remove_last(cls):
        global lb
        lb.delete("end")
    
    @classmethod
    def remove_all(cls):
        global lb
        lb.delete(0, "end")

    @classmethod
    def most_important(cls):
        global lb, eb
        content = f"{eb.get()}                         IMPORTANT"
        lb.insert(0, content)
        eb.delete(0, "end")

        try:
            with open("todo.txt", "a") as f_object:
                f_object.write(content)
        except FileNotFoundError:
            print("This file is not found")
            


    

    def but(self, background, x, width ,text, cmd=None, y=85):
        b = tk.Button(self.screen, text=text, bg=background, font=("Corier", 8, "bold"), borderwidth=5, command=cmd)
        b.place(x=x, y=y, width=width)
    

    

    
    def on_screen(self, x, y, txt, background, foreground="black"):
        t = tk.Label(self.screen, text=txt, bg=background, fg=foreground, font=("Courier", 14, "bold"))
        t.place(x=x, y=y)
    
    def present_file(self):
        global lb
        try:
            with open("todo.txt") as f_read:
                lines = f_read.readlines()
        except FileNotFoundError:
            print("File not found")
        else:
            for line in lines:
                lb.insert("end", line)




todo = App(500, 500)
todo.draw("To-Do List", color=yellow)
todo.on_screen(170, 10, "To Do list app", yellow)
todo.entry_bar(160, 50)
todo.list_box(10, 140, 480, 340)
todo.present_file()

# Add task

todo.but(dark_yellow, 160, 75, "Add Task", App.get_entry)

# Remove task

todo.but(dark_yellow, 260, 75, "Task Done", App.remove_last)

# Remove all


todo.but(dark_yellow, 360, 75, "Rmv all", App.remove_all)

# order


todo.but(dark_yellow, 60, 75, "important", App.most_important)




todo.stay_running()
