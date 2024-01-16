from tkinter import *

class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My App")

        self.label = Label(master, text="This is my app!")
        self.label.pack()

        self.print_button = Button(master, text="Print Me", command=self.print_something)
        self.print_button.pack()

        self.record_button = Button(master, text="Record", command=self.record_mouse_movement)
        self.record_button.pack()

        self.exit_button = Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

    def print_something(self):
        print("Hey whatsup bro, I am doing something very interesting.")

    def record_mouse_movement(self):
        def motion(event):
            x, y = event.x, event.y
            print(f"Mouse position: ({x}, {y})")
        self.master.bind("<Motion>", motion)

root = Tk()
my_app = MyApp(root)
root.mainloop()
