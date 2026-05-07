from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Virus Detected!')
root.geometry('200x200')

def msg():
    messagebox.showwarning('Alert', 'Stop! Virus Found')

btn = Button(text='Scan for Virus', fg='rosybrown', bg='dodgerblue', command=msg, width=10)

btn.place(x=40, y=80)

root.mainloop()