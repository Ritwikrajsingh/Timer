from tkinter import *
from tkinter.ttk import *
from datetime import timedelta, datetime

def set_timer():
	today = datetime.today()
	today_timestamp = int(today.timestamp())
	estimation = datetime(year=today.year, month=int(e2.get()), day=int(e1.get()), hour=0, minute=0, second=0)
	estimation_timestamp = int(estimation.timestamp())
	t = estimation_timestamp - today_timestamp
	if t > 0:
		return t
	else:
		return 0

def countdown():
	t = set_timer()
	if t > 0:
		td = timedelta(seconds=t)
		l1.config(text = td, background= "black")
		t -= 1
		l1.after(1000, countdown)
	else:
		print("end")
		l1.config(text = "Time is up!")

"""User Interface"""

#CANVAS
root = Tk()
root.title("Timer")
root.geometry("220x125")

# LABELS
l1 = Label(root, font = "arial 20", foreground = "red")
l1.grid(row = 1, column = 2, pady=3)

l2 = Label(root, font = "arial 10", text = "DD :")
l2.grid(row = 2, column = 1)

l3 = Label(root, font = "arial 10", text= "MM :")
l3.grid(row = 4, column = 1)

l4 = Label(root,font="arial 20", text='just for paddin',foreground="gray85")
l4.grid(row = 7, column = 2, padx = 25, pady=3)

#INPIT BOXES
day,month = StringVar(),StringVar()

e1 = Entry(root, textvariable = day,)
e1.grid(row = 2,column = 2, pady=2)

e2 = Entry(root, textvariable = month)
e2.grid(row = 4,column = 2, pady=2)

#BUTTONS
#if you want 2 buttons i.e set/stop then you can uncomment below given code
"""
def stop():
	exit()
b1 = Button(root, text = "STOP", command = stop)
b1.grid(row = 5, column = 2, pady=2,padx = 20)
"""
b2 = Button(root, text = "START", command = countdown)
b2.grid(row = 6, column = 2, pady = 15, padx = 20)
#root.mainloop()
mainloop()