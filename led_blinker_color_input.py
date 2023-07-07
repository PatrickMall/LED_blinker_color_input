import RPi.GPIO as GPIO
import time
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Blink Counter')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
number_field = Entry(root, width=35, borderwidth=3)
number_field.pack()

COLORS = [
    ('red'),
    ('yellow'),
    ('green')
]
colorPicked = StringVar()
colorPicked.set('red')

for color in COLORS: 
    Radiobutton(root, text=color, variable=colorPicked, value=color, fg=color).pack()

def button_clicked(numberOfBlinks, colorType):
    number_field.delete(0, END)
    if colorType == 'red':
        for i in range(numberOfBlinks):        
            GPIO.output(7,True)
            time.sleep(0.3)
            GPIO.output(7,False)
            time.sleep(0.3)
    if colorType == 'yellow':
        for i in range(numberOfBlinks):        
            GPIO.output(11,True)
            time.sleep(0.3)
            GPIO.output(11,False)
            time.sleep(0.3)
    if colorType == 'green':
        for i in range(numberOfBlinks):        
            GPIO.output(13,True)
            time.sleep(0.3)
            GPIO.output(13,False)
            time.sleep(0.3)

button_select = Button(root, text="Select", fg="white", bg="gray" , command=lambda: button_clicked(int(number_field.get()), colorPicked.get()))
button_select.pack()
root.mainloop()