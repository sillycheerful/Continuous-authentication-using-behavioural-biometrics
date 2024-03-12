from tkinter import *
import time
import random
#from pynput import mouse 
from pynput.mouse import Controller
from pynput import keyboard 
import timeit

key_press_count = 0
interval_start_time_keyboard = time.time()
mouse = Controller()


class MyApp:
    def __init__ (self, root):
        self.create_primary_window()
        
        """ listener = mouse.Listener(
            on_move=self.on_move)
        listener.start() """
        speed_in_pixels_per_second = self.measure_mouse_speed(interval_seconds=10)
        print(f"Average mouse speed: {speed_in_pixels_per_second:.2f} pixels/second")

        listener = keyboard.Listener(
            on_press=self.on_press)
        listener.start()
        
        for i in range(3):
            x= random.randint(3000, 120000)
            root.after(x, self.create_secondary_window)
        
    def create_primary_window(self):
        self.root = root
        self.root.title("My App")
        self.root.geometry("200x200")
        self.print_button = Button(self.root, text="Print Me", command=self.print_something)
        self.print_button.pack()
        
        self.exit_button = Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

        input_from_user= Entry(self.root)
        input_from_user.pack()

    """ def on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y))) """
    
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

    """ def record_mouse_movement(self):
        def motion(event):
            x, y = event.x, event.y
            print(f"Mouse position: ({x}, {y})")
            self.root.bind("<Motion>", motion) """
        
    def measure_mouse_speed(self, interval_seconds=10):
        start_time = time.time()
        total_distance = 0

        while True:
            current_position = mouse.position
            #time.sleep(0.01)  # Small delay to avoid excessive CPU usage
            new_position = mouse.position

            distance = ((new_position[0] - current_position[0])**2 +
                        (new_position[1] - current_position[1])**2)**0.5
            total_distance += distance

            elapsed_time = time.time() - start_time
            if elapsed_time >= interval_seconds:
                break

        average_speed = total_distance / elapsed_time
        return average_speed

    def on_press(self, event):
        global key_press_count, interval_start_time_keyboard
        key_press_count += 1
        current_time_keyboard = time.time()

        # Check if 10 seconds have elapsed
        if current_time_keyboard - interval_start_time_keyboard >= 10:
            print(f"Keys pressed in the last 10 seconds: {key_press_count}")
            key_press_count = 0  # Reset the counter for the next interval
            interval_start_time_keyboard = current_time_keyboard
        
    """ def speed(self, x, y):
        distance = x, y 
        time=0
        speed = distance/time
        #so for mouse if i do speed of 500 ms howmany pixels movement
        #for keyboard if i do speed how many keys pressed in 10 seconds
 """
root = Tk()
my_app = MyApp(root)
root.mainloop()
