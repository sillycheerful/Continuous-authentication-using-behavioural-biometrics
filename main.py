from tkinter import *
import time
import random
from pynput import mouse 
from pynput import keyboard 

key_press_count = 0
interval_start_time_keyboard = time.time()
close_time_pop_up = time.time()

class MyApp:
    def __init__ (self, root):
        self.create_primary_window()
        
        listener = mouse.Listener(
            on_move=self.on_move)
        listener.start() 

        listener = keyboard.Listener(
            on_press=self.on_press)
        listener.start()
        i=1
        for i in range(3):
            delay_Time= random.randint(3000, 120000)
            start_time_pop_up = time.time()
            root.after(delay_Time, self.create_secondary_window)
            close_time_pop_up = time.time()
            with open("Participant_X_pop_up_time.txt","a") as file:
                file.write(f"Pop up {i+1} appeared after {start_time_pop_up} and was closed after {close_time_pop_up} \n")
            i+=1
        
    def create_primary_window(self):
        self.root = root
        self.root.title("My App")
        self.root.geometry("200x200")
        self.print_button = Button(self.root, text="Print Me", command=self.print_something)
        self.print_button.pack()
        
        self.exit_button = Button(self.root, text="Exit",command= lambda:[ self.save_text(input_from_user), self.root.quit()])
        self.exit_button.pack()

        input_from_user= Entry(self.root)
        input_from_user.pack()

    def save_text(self, input_from_user):
        with open("Participant_X_typed_input.txt","a") as file:
            file.write(input_from_user.get() + "\n")
    
    def create_secondary_window(self):
        global close_time_pop_up
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

        #close_time_pop_up = time.time()
        #return close_time_pop_up

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
                #come back to this
                with open("Participant_X_mouse_speed.txt","a") as file:
                    file.write(f"Average speed in the last 10 seconds: {average_speed}\n")
                break
   
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
