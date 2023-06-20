import pyautogui
import time
import random
import pysimplegui

def randomNumber():
    return random.uniform(0.1712, 0.24)

filename = "text.txt"

try:
    with open(filename, 'r') as file:
        textInput = file.read().strip()
except FileNotFoundError:
    print("File not found.")
    exit()

arrayTextInput = list(textInput)

print("This is the content of the file:\n" + textInput)
print("Are you sure you want to type this?")
yesNoInput = input("y/n: ")

answer = True if yesNoInput.lower() == "y" else False

intCounter = 0
if answer:
    time.sleep(3)
    while len(arrayTextInput) > intCounter:
        if(arrayTextInput[intCounter] == " "):
            time.sleep(randomNumber() * 0.5)
        pyautogui.write(arrayTextInput[intCounter])
        #time.sleep(randomNumber() * 0.0025)
        intCounter += 1
        


