# Cleaned up code with more descriptive constant names

import time
import random
import threading
import customtkinter
from tkinter import *

# Constants
INITIAL_TYPING_SPEED = 0.1  # The initial typing speed specified in seconds per character.
INITIAL_WORDS_PER_MINUTE = 60  # The initial typing speed specified in words per minute.
PRINT_TOGGLE = True  # Boolean flag to control the printing status.

# Parameters for random pauses between a range of characters.
CHARACTER_PAUSE_MIN = 60  # The minimum limit for character pause.
CHARACTER_PAUSE_MAX = 150  # The maximum limit for character pause.
REST_PERIOD_MIN = 3  # The minimum limit for rest period.
REST_PERIOD_MAX = 10  # The maximum limit for rest period.

# Parameters to control the probability of a pause occurring between words.
WORD_PAUSE_MIN = 1  # The minimum limit for word pause.
WORD_PAUSE_MAX = 2  # The maximum limit for word pause.

# Parameters to determine the chance of a pause occurring between words.
NUMBER_FOR_CHANCE = 2  # A random number compared to for a pause chance.
CHANCE_WORD_PAUSE_MIN = 1  # The minimum limit for the chance of word pause.
CHANCE_WORD_PAUSE_MAX = 5  # The maximum limit for the chance of word pause.

# Functions

def generate_random_number(min_value, max_value, number_type):
    if number_type == 0:
        return random.uniform(min_value, max_value)
    elif number_type == 1:
        return random.randint(min_value, max_value)

def print_text():
    global PRINT_TOGGLE
    global typing_speed
    text_input = my_entry.get(1.0, END)
    text_input_list = list(text_input)
    counter = 0
    cool_down_timer = 0
    time.sleep(2)
    character_pause = generate_random_number(CHARACTER_PAUSE_MIN, CHARACTER_PAUSE_MAX, 1)

    for char in text_input_list:
        if not PRINT_TOGGLE:
            PRINT_TOGGLE = True
            return
        if char == " " and human_mode.get():
            pause_time = generate_random_number(typing_speed/2, typing_speed*2, 0)
            time.sleep(pause_time)
            print(pause_time)
        pyautogui.write(char, interval=typing_speed)
        counter += 1
        cool_down_timer += 1
        if cool_down_timer == character_pause and human_mode.get():
            y = time.sleep(generate_random_number(REST_PERIOD_MIN, REST_PERIOD_MAX, 0))
            print(y)
            cool_down_timer = 0
            character_pause = generate_random_number(CHARACTER_PAUSE_MIN, CHARACTER_PAUSE_MAX, 1)
        if char == " " and NUMBER_FOR_CHANCE == generate_random_number(CHANCE_WORD_PAUSE_MIN, CHANCE_WORD_PAUSE_MAX, 1) and human_mode.get():
            time.sleep(generate_random_number(WORD_PAUSE_MIN, WORD_PAUSE_MAX, 0))

def stop_typing():
    global PRINT_TOGGLE
    PRINT_TOGGLE = False
    return

def clear_text():
    my_entry.delete(1.0, END)

def adjust_typing_speed(wpm):
    global typing_speed
    words_per_minute = int(wpm)
    typing_speed = 60 / (words_per_minute * 5)  # based on the standard definition of wpm

def update_slider(wpm):
    adjust_typing_speed(wpm)
    wpm_label.configure(text =str(wpm) +" (WPM)")

# Main Code

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title('AutoTyper')
root.geometry("620x470")

human_mode = BooleanVar(value=True)  # initial human typing mode, created after root window

my_labelframe = customtkinter.CTkFrame(root, corner_radius=10)
my_labelframe.pack(pady=10)

text_frame = customtkinter.CTkFrame(root, corner_radius=10)
text_frame.pack(pady=10)

my_entry = Text(text_frame, height=20, width=67, wrap=WORD, bd=0, bg="#292929", fg="silver")
my_entry.grid(row=0, column=0, pady=10)

start_button = customtkinter.CTkButton(my_labelframe, text="Start Typing", command=lambda: threading.Thread(target=print_text).start())
start_button.grid(row=1, column=0, padx=1, pady=10)

stop_button = customtkinter.CTkButton(my_labelframe, text="Stop Typing", command=stop_typing)
stop_button.grid(row=1, column=1, padx=1, pady=10)

clear_button = customtkinter.CTkButton(my_labelframe, text="Clear", command=clear_text)
clear_button.grid(row=1, column=2, padx=1, pady=10)

# Typing speed slider
speed_label = customtkinter.CTkLabel(my_labelframe, text="Typing Speed (WPM):")
speed_label.grid(row=2, column=0)
speed_scale = customtkinter.CTkSlider(my_labelframe, number_of_steps=22, from_=10, to=120, orientation=HORIZONTAL, command=update_slider)
speed_scale.set(INITIAL_WORDS_PER_MINUTE)
speed_scale.grid(row=2, column=1)

# Displayed Typing speed
wpm_label = customtkinter.CTkLabel(my_labelframe, text= str(INITIAL_WORDS_PER_MINUTE) +" (WPM)")
wpm_label.grid(row=2, column=2)

# Human typing mode toggle
human_mode_toggle = customtkinter.CTkCheckBox(my_labelframe, text="Human Typing Mode", variable=human_mode)
human_mode_toggle.grid(row = 3, column = 0)

root.mainloop()

