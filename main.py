from tkinter import *
import time
import random
from pynput import mouse 
#from pynput.mouse import Controller
from pynput import keyboard 
#import timeit

key_press_count = 0
interval_start_time_keyboard = time.time()
#mouse = Controller()
interval_start_time_mouse = time.time()

class MyApp:
    def __init__ (self, root):
        self.create_primary_window()
        
        listener = mouse.Listener(
            on_move=self.on_move)
        listener.start() 
        
        #self.measure_mouse_speed()

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
    
    def on_move(self, x, y):
        start_time = time.time()
        total_distance = 0
        with open("Participant_X_mouse_movements.txt","a") as file:
            file.write(f'Pointer moved to: {x,y}\n') 
            
        while True:
            current_position = x,y
            time.sleep(0.01)  # Small delay to avoid excessive CPU usage
            new_position = x,y
            distance = ((new_position[0] - current_position[0])**2 +
                        (new_position[1] - current_position[1])**2)**0.5
            total_distance += distance

            elapsed_time = time.time() - start_time
            if elapsed_time >= 10:
                average_speed = total_distance / elapsed_time
                print(average_speed, new_position,current_position,elapsed_time)
                break

    """ def measure_mouse_speed(self):
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
            if elapsed_time >= 10:
                break

        average_speed = total_distance / elapsed_time
        return average_speed """
    
    """ def measure_mouse_speed(self)#changed:
        global interval_start_time_mouse
        current_time_mouse = time.time()
        total_distance = 0

        while True:
            current_position = mouse.position
            #time.sleep(0.01)  # Small delay to avoid excessive CPU usage
            new_position = mouse.position

            distance = ((new_position[0] - current_position[0])**2 +
                        (new_position[1] - current_position[1])**2)**0.5
            total_distance += distance

            #elapsed_time = time.time() - start_time
            elapsed_time= current_time_mouse-interval_start_time_mouse
            if elapsed_time >= 10:
                average_speed = total_distance / elapsed_time
                with open("Participant_X.txt","a") as file:
                    file.write(f"Average mouse speed: {average_speed:.2f} pixels/second\n")
                total_distance = 0
                interval_start_time_mouse = current_time_mouse """


    def on_press(self, event):
        global key_press_count, interval_start_time_keyboard
        key_press_count += 1
        current_time_keyboard = time.time()

        # Check if 10 seconds have elapsed
        if current_time_keyboard - interval_start_time_keyboard >= 10:
            with open("Participant_X_type_speed.txt","a") as file:
                file.write(f"Keys pressed in the last 10 seconds: {key_press_count}\n")
            key_press_count = 0  # Reset the counter for the next interval
            interval_start_time_keyboard = current_time_keyboard
        
root = Tk()
my_app = MyApp(root)
root.mainloop()
