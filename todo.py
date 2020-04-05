""" Simple todo list GUI python app """
import tkinter as tk
import datetime
from tkinter import messagebox


yellow = "#F7FF45"
dark_yellow = "#AFB438"

class App(object):
    """ Making the app class """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = "root"

    def draw(self, title, color="#FFFFFF"):
        """ Drawing the the window and giving some details """
        self.screen = tk.Tk()
        self.screen.geometry(f"{self.width}x{self.height}")
        self.screen.config(bg=color)
        self.screen.title(title)
    
    def stay_running(self):
        self.screen.mainloop()

    def list_box(self, x, y, width, height):
        """ Making a list box and placing it (To place the tasks in it) """
        global lb
        lb = tk.Listbox(self.screen)
        lb.place(x=x, y=y, width=width, height=height)


    def entry_bar(self, x, y, width=180):
        """ Making an entry bar and placing it """
        global eb
        eb = tk.Entry(self.screen, borderwidth=5)
        eb.place(x=x, y=y, width=width)
    
    """ Making 4 classmethods for each button """
    @classmethod
    def get_entry(cls):
        """ Getting input from entry bar, displaying it in the list boc, and writing it into the file. """
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
        """ Delete the last task added from the listbox """
        global lb
        lb.delete("end")

        with open("todo.txt") as f:
            lines = f.readlines()
        lines = lines[:-1]
        print(lines)
        with open("todo.txt", "w") as f_w:
            f_w.writelines(lines)

        
    
    @classmethod
    def remove_all(cls):
        """ Remove all tasks from the listbox and the todo.txt file file. """
        global lb
        lb.delete(0, "end")
        try:
            with open("todo.txt", "w") as f_erase:
                f_erase.write("")
        except FileNotFoundError:
            print("File not Found")

    @classmethod
    def most_important(cls):
        """ Inserting an important task, and writing ot to the file. """
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
        """ Button object, since we have 4 buttons. """
        b = tk.Button(self.screen, text=text, bg=background, font=("Corier", 8, "bold"), borderwidth=5, command=cmd)
        b.place(x=x, y=y, width=width)
    

    

    
    def on_screen(self, x, y, txt, background, foreground="black"):
        """ Putting text on screen """
        t = tk.Label(self.screen, text=txt, bg=background, fg=foreground, font=("Courier", 14, "bold"))
        t.place(x=x, y=y)
    
    def present_file(self):
        """ Reads the todo.txt file when the program is opened. """
        global lb
        try:
            with open("todo.txt") as f_read:
                lines = f_read.readlines()
        except FileNotFoundError:
            print("File not found")
        else:
            for line in lines:
                lb.insert("end", line)



""" Making an instance of the app class and using its methods. """
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
