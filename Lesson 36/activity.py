from tkinter import *
from datetime import date

root = Tk()
root.title('Widgets')
root.geometry('400x300')
lbl = Label(text = "Hey there!", fg='white', bg = 'green', height=1, width=300)
name_lbl = Label(text='Full name', bg='grey')
name_entry = Entry()
text_box = Text(height=3)
def display():
    user_input = name_entry.get()
    global message
    greet = 'Hello, ' + user_input + '. '

    message = "Welcome to the application\nToday's date is "
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

btn = Button(text='Begin', command=display, height=1, fg='white', bg='teal')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()