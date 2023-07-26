import pyautogui
import time
import random
from tkinter import *
import customtkinter

printToggle=True
typing_speed = 0.1  # initial typing speed in seconds per character
words_per_minute = 60  # initial words per minute

def randomNumber(x, y, type):
    if type == 0:
        return random.uniform(x, y)
    elif type == 1:
        return random.randint(x, y)

def getTextthenPrint():
    global printToggle
    global typing_speed
    textInput= my_entry.get(1.0, END)
    print("\n\nThis is the content of the Entry:\n" + textInput)

    arrayTextInput = list(textInput)

    yesNoInput ="y"
    answer = yesNoInput.lower() == "y"

    intCounter = 0
    intCoolDownTimer = 0
    if answer:
        time.sleep(5)
        longPause = randomNumber(40, 50, 1)
        if printToggle:
            while len(arrayTextInput) > intCounter:
                if arrayTextInput[intCounter] == " " and human_mode.get():
                    x = randomNumber(typing_speed/2, typing_speed*2, 0)
                    time.sleep(x)
                    print(x)
                pyautogui.write(arrayTextInput[intCounter], interval=typing_speed)
                intCounter += 1
                intCoolDownTimer += 1
                if intCoolDownTimer == longPause and human_mode.get():
                    y = time.sleep(randomNumber(8, 15, 0))
                    print(y)
                    intCoolDownTimer = 0
                    longPause = randomNumber(40,50,1)
                if arrayTextInput[intCounter] == " " and 2 == randomNumber(1, 5, 1) and human_mode.get():
                    time.sleep(randomNumber(2, 5, 0))
        else:
             printToggle= True

def fakeExit():
    global printToggle
    printToggle=False
    return

def Clear():
    my_entry.delete(1.0, END)

def adjust_typing_speed(wpm):
    global typing_speed
    words_per_minute = int(wpm)
    typing_speed = 60 / (words_per_minute * 5)  # based on the standard definition of wpm
    
def Update_slider(wpm):
    adjust_typing_speed(wpm)
    WPM_label.configure(text =str(wpm) +" (WPM)")

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

Start_button = customtkinter.CTkButton(my_labelframe, text="Start Typing", command=getTextthenPrint)
Start_button.grid(row=1, column=0, padx=1, pady=10)

Stop_button = customtkinter.CTkButton(my_labelframe, text="Stop Typing", command=fakeExit)
Stop_button.grid(row=1, column=1, padx=1, pady=10)

Clear_button = customtkinter.CTkButton(my_labelframe, text="Clear", command=Clear)
Clear_button.grid(row=1, column=2, padx=1, pady=10)

# Typing speed slider
speed_label = Label(my_labelframe, text="Typing Speed (WPM):")
speed_label.grid(row=2, column=0)
speed_scale = customtkinter.CTkSlider(my_labelframe, number_of_steps=22,from_=10, to=120, orientation=HORIZONTAL, command=Update_slider)
speed_scale.set(words_per_minute)
speed_scale.grid(row=2, column=1)

# Displayed Typing speed
WPM_label = Label(my_labelframe, text= str(words_per_minute) +" (WPM)")
WPM_label.grid(row=2, column=2)


# Human typing mode toggle
human_mode_toggle = Checkbutton(my_labelframe, text="Human Typing Mode", variable=human_mode)
human_mode_toggle.grid(row=3, column=0)

root.mainloop()
