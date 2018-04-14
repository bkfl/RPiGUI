from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

# Outputs
ledRed = LED(16)
ledGreen = LED(20)
ledBlue = LED(21)

# GUI
win = Tk()
win.title("RPi: Making a GUI")

# Functions
def switchLed():
    if rbVal.get() == "red":
        ledRed.on()
        ledGreen.off()
        ledBlue.off()
    elif rbVal.get() == "green":
        ledRed.off()
        ledGreen.on()
        ledBlue.off()
    elif rbVal.get() == "blue":
        ledRed.off()
        ledGreen.off()
        ledBlue.on()
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
# Widgets
rbVal = StringVar()
rbRed = Radiobutton(win, command = switchLed, text = "Red", value = "red", variable = rbVal, width = 10)
rbRed.grid(row=0, column=0)
rbGreen = Radiobutton(win, command = switchLed, text = "Green", value = "green", variable = rbVal, width = 10)
rbGreen.grid(row=0, column=1)
rbBlue = Radiobutton(win, command = switchLed, text = "Blue", value = "blue", variable = rbVal, width = 10)
rbBlue.grid(row=0, column=2)
btnExit = Button(win, command = close, text = "Exit", width = 15)
btnExit.grid(row=1, columnspan=3)

# init
rbRed.invoke()
