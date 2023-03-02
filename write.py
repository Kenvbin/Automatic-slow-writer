import random
import pyautogui
import time
import os
import keyboard

os.system("cls")

write = []

print("paste what you want to write")
imput = input(": ")

for character in imput:
    write.append(character)

print("press right control when you're ready")
while True:
    if keyboard.is_pressed("right ctrl"):
        break

os.system("cls")

for item in write:
    secs =  random.randint(0,2)
    secs = secs / 10
    if item == " ":
        pyautogui.press("space")
    else:
        pyautogui.press(item)
    time.sleep(secs)

print("done")