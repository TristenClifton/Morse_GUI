from Tkinter import *

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) # Ignore warning
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.OUT)

def Dot():
	GPIO.output(3, GPIO.HIGH)
	time.sleep(0.4)
	GPIO.output(3, GPIO.LOW)
	time.sleep(0.4)

def Dash():
	GPIO.output(3, GPIO.HIGH)
	time.sleep(1.2)
	GPIO.output(3, GPIO.LOW)
	time.sleep(0.4)
	
def Delay():
	GPIO.output(3, GPIO.LOW)
	time.sleep(1.2)

def BlinkInMorseCode(word):
	for x in word:
		Delay()
		if(x == "A" or x == "a"):
			Dot()
			Dash()
		if(x == "B" or x == "b"):
			Dash()
			Dot()
			Dot()
			Dot()
		if(x == "C" or x == "c"):
			Dash()
			Dot()
			Dash()
			Dot()			
		if(x == "D" or x == "d"):
			Dash()
			Dot()
			Dot()
		if(x == "E" or x == "e"):
			Dot()
		if(x == "F" or x == "f"):
			Dot()
			Dot()
			Dash()
			Dot()
		if(x == "G" or x == "g"):
			Dash()
			Dash()
			Dot()
		if(x == "H" or x == "h"):
			Dot()
			Dot()
			Dot()
			Dot()
		if(x == "I" or x == "i"):
			Dot()
			Dot()
		if(x == "J" or x == "j"):
			Dot()
			Dash()
			Dash()
			Dash()
		if(x == "K" or x == "k"):
			Dash()
			Dot()
			Dash()
		if(x == "L" or x == "l"):
			Dot()
			Dash()
			Dot()
			Dot()
		if(x == "M" or x == "m"):
			Dash()
			Dash()
		if(x == "N" or x == "n"):
			Dash()
			Dot()
		if(x == "O" or x == "o"):
			Dash()
			Dash()
			Dash()
		if(x == "P" or x == "p"):
			Dot()
			Dash()
			Dash()
			Dot()
		if(x == "P" or x == "p"):
			Dot()
			Dash()
			Dash()
			Dot()			
		if(x == "Q" or x == "q"):
			Dash()
			Dash()
			Dot()
			Dash()
		if(x == "R" or x == "r"):
			Dot()
			Dash()
			Dot()
		if(x == "S" or x == "s"):
			Dot()
			Dot()
			Dot()
		if(x == "T" or x == "t"):
			Dash()
		if(x == "U" or x == "u"):
			Dot()
			Dot()
			Dash()
		if(x == "V" or x == "v"):
			Dot()
			Dot()
			Dot()
			Dash()
		if(x == "W" or x == "w"):
			Dot()
			Dash()
			Dash()
		if(x == "X" or x == "x"):
			Dash()
			Dot()
			Dot()
			Dash()
		if(x == "Y" or x == "Y"):
			Dash()
			Dot()
			Dash()
			Dash()
		if(x == "Z" or x == "Z"):
			Dash()
			Dash()
			Dot()
			Dot()

 
root = Tk()
root.geometry("300x150")
root.title("Morse Code Blinker")
 
blinkedText = ""

def Take_input():
	blinkedText = inputtxt.get("1.0", "end-1c")
	if(len(blinkedText) > 12):
		warningMessageText.config(text = "Max Length Exceeded", fg = "RED")
	else:		
		Output.delete("1.0", END)
		Output.insert(END, blinkedText)
		time.sleep(0.2)
		BlinkInMorseCode(blinkedText)
        
header = Label(text = "Enter a word to blink, max 12 characters:")
warningMessageText = Label(text = "", fg = "RED")
body= Label(text = "Currently Blinking:")
inputtxt = Text(root, height = 1,
                width = 15,
                bg = "light yellow")
 
Output = Text(root, height = 1,
              width = 15,
              bg = "light cyan")
 
Display = Button(root, height = 2,
                 width = 15,
                 text ="BLINK!",
                 command = lambda:Take_input())
                 
Output.insert(END, ' ')
 
header.pack()
inputtxt.pack()
warningMessageText.pack()
body.pack()
Output.pack()
Display.pack()

mainloop()
