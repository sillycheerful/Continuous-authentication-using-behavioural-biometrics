from tkinter import *

class MyApp:
    def __init__ (self, root):
        self.root = root
        self.root.title("My App")
        self.root.geometry("200x200")


        self.label = Label(self.root, text="This is my app!")
        self.label.pack()

        self.print_button = Button(self.root, text="Print Me", command=self.print_something)
        self.print_button.pack()

    #doesnt currently work lol
        self.record_button = Button(self.root, text="Record", command=self.record_mouse_movement)
        self.record_button.pack()

        self.exit_button = Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

        for i in range(3):
            self.create_secondary_window()

    def create_secondary_window(self):
        self.secondary_window= Toplevel(self.root)
        self.secondary_window.title("Speed is being recorded")
        self.secondary_window.geometry("100x100")

        self.secondary_window_lable= Label(self.secondary_window,text="this is my 2nd window")
        self.secondary_window_lable.pack()

        self.secondary_window_button=Button(self.secondary_window, text="Ok", command=self.secondary_window.destroy)
        self.secondary_window_button.pack()

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


