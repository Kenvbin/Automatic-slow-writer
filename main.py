import random
import threading
import time
from tkinter import *
from tkinter import filedialog, ttk

import keyboard

interface = Tk()

interface.title("Automatic Slow Writer")

interface.geometry("200x150")
interface.minsize(200, 150)
interface.maxsize(200, 150)

letters = []
iterate = 0
not_stopped = True

#with help from https://www.geeksforgeeks.org/python/read-a-text-file-using-python-tkinter/
def openfile():
    
    global letters, not_stopped, iterate
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    if file_path:
        letters = []
        not_stopped = False
        with open(file_path,'r') as file:
            content = file.read()
            for character in content:
                letters.append(character)
        iterate = 0

def write_the_text():
    
    global letters, iterate, not_stopped  # noqa: PLW0602

    print("Started")

    not_stopped = True

    for i in range(10):
        if not not_stopped:
            break
        time.sleep(.1)

    to_iterate = letters[iterate:len(letters)]
    for item in to_iterate:
        
        if not not_stopped:
            break
        
        secs =  random.randint(0,200)
        secs = secs / 1000

        keyboard.write(item)
        
        if item == " " and random.randint(0,15) == 2:    
            for i in range(50):
                if not not_stopped:
                    break
                time.sleep(0.1)
        
        time.sleep(secs)

        iterate += 1
    not_stopped = False

def stoptext():
    global iterate, not_stopped
    
    print("Stopped")
    iterate = 0
    not_stopped = False

def pausetext():
    global not_stopped
    
    print("Paused")
    not_stopped = False

def writetext():
    global not_stopped  # noqa: PLW0602
    
    if not_stopped == False:
        threading.Thread(target=write_the_text, daemon=True).start()

button = ttk.Button(interface, text="Open", command=openfile)
button.pack(pady = 2)

start = ttk.Button(interface, text="Start - Ctrl", command=writetext)
start.pack(pady = 2)

stop = ttk.Button(interface, text="Stop - Caps Lock", command=stoptext)
stop.pack(pady = 2)

pause = ttk.Button(interface, text="Pause - Shift", command=pausetext)
pause.pack(pady = 2)

keyboard.add_hotkey("right ctrl", writetext)
keyboard.add_hotkey("right shift", pausetext)
keyboard.add_hotkey("caps lock", stoptext)


interface.mainloop()