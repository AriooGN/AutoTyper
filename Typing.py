#Code Related
import pyautogui
import time
import random

#GUI Related
from tkinter import *
import customtkinter


#Initilize Instance Variables
filename = "text.txt"
printToggle=True

#Varying Print Time Range
def randomNumber():
    return random.uniform(0.1712, 0.24)

#Pull Text From File and Returns a textInput
def readFile():
        try:
            with open(filename, 'r') as file:
                textInput = file.read().strip()
                if textInput=="":
                    print("\nThere is no contents in the file\n")
                    return None
                else:
                    return textInput     
        except FileNotFoundError:
            print("File not found.")
            exit()
    

#Function that Pulls text and Begins Typing
def getTextthenPrint():
    global printToggle

    #CheckFile Contents First if none then use Text Box
    if (readFile()!=None):
        textInput=readFile()
        print("\n\nThis is the content of the file:\n" + textInput)
    else:
        textInput= my_entry.get(1.0, END)
        print("\n\nThis is the content of the Entry:\n" + textInput)
        

    arrayTextInput = list(textInput)


    #print("Are you sure you want to type this?")
    #yesNoInput = input("y/n: ")
    yesNoInput ="y"

    answer = True if yesNoInput.lower() == "y" else False

    intCounter = 0
    if answer:
        time.sleep(5)
        if( printToggle== True):
            while len(arrayTextInput) > intCounter:
                if(arrayTextInput[intCounter] == " "):
                    time.sleep(randomNumber() * 0.5)
                pyautogui.write(arrayTextInput[intCounter])
                #time.sleep(randomNumber() * 0.0025)
                intCounter += 1
        else:
             printToggle= True

def fakeExit():
    global printToggle
    printToggle=False
    return   

#GUI Starting

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('AutoTyper')

#Change Icon Image
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("620x470")

def Clear():
	# Clear The text
	my_entry.delete(1.0, END)

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

root.mainloop()
