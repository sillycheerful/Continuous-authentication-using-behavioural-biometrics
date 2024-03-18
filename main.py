from tkinter import *
import time
import random
from pynput import mouse, keyboard


class MyApp:
    """
    Explain what this does
    """

    def __init__(self, root):
        self.root = root
        self.create_primary_window()
        self.key_press_count = 0
        self.interval_start_time_keyboard = time.time()

        # Defining instance variables here (used in create_secondary_window and start_recording method)
        self.start_time_pop_up = 0
        self.close_time_pop_up = 0

        self.pop_up_times = []
        self.keyboard_press_count = []
        self.mouse_movements = []

        self.mouse_listener = mouse.Listener(on_move=self.on_move)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)

    def start_recording(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()

        pop_up_number = 0
        while pop_up_number < 3:
            delay_time = random.randint(3000, 120000)
            self.root.after(delay_time, self.create_secondary_window)
            pop_up_number += 1

    def save_times(self):
        with open(
            file="Participant_X_pop_up_time.txt",
            mode="a",
            encoding="utf-8"
        ) as file:
            for i in range(len(self.pop_up_times)):
                file.write(
                    f"Pop up {i+1} appeared after {self.pop_up_times[i][0]} and was closed after {self.pop_up_times[i][1]} \n")

        with open(
            file="Participant_X_type_speed.txt",
            mode="a",
            encoding="utf-8"
        ) as file:
            for i in range(len(self.keyboard_press_count)):
                file.write(
                    f"{self.keyboard_press_count[i]}\n")

        # Separate entries in self.mouse_movements by every 10 seconds
        # Then add a line to the file for each entry
        with open(
            file="Participant_X_mouse_movements.txt",
            mode="a",
            encoding="utf-8"
        ) as file:
            current_time = self.mouse_movements[0][0]
            for i in range(len(self.mouse_movements)):
                file.write(
                    f" {self.mouse_movements[i][1], self.mouse_movements[i][2]}\n")
                # if 10 seconds has passed
                if self.mouse_movements[i][0] - current_time >= 10:
                    current_time = self.mouse_movements[i][0]
                    file.write(
                        f"{'_' *30}\n")

    def create_primary_window(self):
        self.root.title("Please click 'Start Recording' to begin the test.")
        self.root.geometry("500x100")
        self.record_button = Button(
            self.root, text="Start recording", command=self.start_recording)
        self.record_button.pack()

        input_from_user = Entry(self.root, width=100)
        input_from_user.pack(padx=10, pady=10)

        def exit_program():
            self.save_text(input_from_user)
            self.save_times()
            self.root.quit()

        # self.exit_button = Button(self.root, text="Exit", command=lambda: [
        #                           self.save_text(input_from_user), self.root.quit()])
        exit_button = Button(self.root, text="Exit", command=exit_program)
        exit_button.pack()

    def save_text(self, input_from_user):
        with open("Participant_X_typed_input.txt", "a") as file:
            file.write(input_from_user.get() + "\n")

    def create_secondary_window(self):
        """
        Creates a secondary window with a label and a button.
        This is for ...
        """
        self.start_time_pop_up = time.time()

        secondary_window = Toplevel(self.root)
        secondary_window.title("Speed is being recorded")
        secondary_window.geometry("300x100")

        secondary_window_label = Label(
            secondary_window, text="This is a pop up window")
        secondary_window_label.pack()

        def close_secondary_window():
            self.close_time_pop_up = time.time()
            self.pop_up_times.append(
                (self.start_time_pop_up, self.close_time_pop_up))  # to get the first part: self.pop_up_times[0][0]
            secondary_window.destroy()

        secondary_window_button = Button(
            secondary_window, text="Ok", command=close_secondary_window)
        secondary_window_button.pack()


    def on_move(self, x, y):
        current_time_mouse = time.time()
        current_list = [current_time_mouse, x, y]
        self.mouse_movements.append(current_list)

    def on_press(self, _):
        """
        Say what this does
        """
        self.key_press_count += 1
        current_time_keyboard = time.time()

        # Check if 10 seconds have elapsed
        if current_time_keyboard - self.interval_start_time_keyboard >= 10:
            self.keyboard_press_count.append(self.key_press_count)
            self.key_press_count = 0  # Reset the counter for the next interval
            self.interval_start_time_keyboard = current_time_keyboard


win = Tk()
my_app = MyApp(win)
win.mainloop()
