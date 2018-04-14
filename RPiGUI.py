from tkinter import *
from tkinter import messagebox
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

# OUTPUTS
led = LED(21)

# GUI
root = Tk()
root.title("RPi: Morse Code")

# EVENT FUNCTIONS
def blink():
    input = eInput.get()
    # Check input is between 1 and 12 characters
    if (1 < len(input) < 13):
        # Check string contains letters only
        if (input.isalpha()):
            
        else:
            messagebox.showinfo("Error", "Input must contain only letters.")
    else:
        messagebox.showinfo("Error", "Input must be 1 to 12 characters.")

def close():
    RPi.GPIO.cleanup()
    root.destroy()

# FUNCTIONS
def morseDot():
    
def morseDash():

def morseCharRest():
    

def morseBlink(char):


# WIDGETS
lbl1 = Label(root, text="Enter a word (12 char max):")
lbl1.pack()
eInput = Entry(root)
eInput.pack()
btnBlink = Button(root, text="Blink It!", command=blink)
btnBlink.pack()
btnClose = Button(root, text="Close", command=close)
btnClose.pack()
