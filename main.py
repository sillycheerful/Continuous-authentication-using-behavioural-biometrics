from tkinter import *
import time
import random


class MyApp:
    def __init__ (self, root):
        self.create_primary_window()
        for i in range(3):
            x= random.randint(3000, 120000)
            root.after(x, self.create_secondary_window)
            

    def create_primary_window(self):
        self.root = root
        self.root.title("My App")
        self.root.geometry("200x200")
        self.print_button = Button(self.root, text="Print Me", command=self.print_something)
        self.print_button.pack()
        #doesnt currently work lol
        # self.record_button = Button(self.root, text="Record", command=self.record_mouse_movement)
        # self.record_button.pack()

        # self.exit_button = Button(self.root, text="Exit", command=self.root.quit)
        # self.exit_button.pack()

        # self.text_window()
        self.exit_button = Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()
        
        input_from_user= Entry(self.root)
        input_from_user.pack()


    def create_secondary_window(self):
        """
        Creates a secondary window with a label and a button.
        This is for ...
        """
        secondary_window= Toplevel(self.root)
        secondary_window.title("Speed is being recorded")
        secondary_window.geometry("100x100")

        secondary_window_lable= Label(secondary_window,text="this is my 2nd window")
        secondary_window_lable.pack()

        secondary_window_button=Button(secondary_window, text="Ok", command=secondary_window.destroy)
        secondary_window_button.pack()

    def print_something(self):
        print("Printing something...")

    def record_mouse_movement(self):
        def motion(event):
            x, y = event.x, event.y
            print(f"Mouse position: ({x}, {y})")
            self.root.bind("<Motion>", motion)

root = Tk()
my_app = MyApp(root)
root.mainloop()
