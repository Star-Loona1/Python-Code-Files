from tkinter import *
from datetime import datetime

root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

label1 = Label(text='Name', fg='snow', bg='navy', width=12)
label2 = Label(text='Date', fg='snow', bg='navy', width=12)
label3 = Label(text='Month', fg='snow', bg='navy', width=12)
label4 = Label(text='Year', fg='snow', bg='navy', width=12)

name_entry = Entry(fg='black', bg='grey')
date_entry = Entry(fg='black', bg='grey')
month_entry = Entry(fg='black', bg='grey')
year_entry = Entry(fg='black', bg='grey')

def display():
    name = name_entry.get()
    date = int(date_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    current_year = datetime.now().year
    age = current_year - year

    greet = 'Hello, ' + name + '.\n'
    message = 'You are ' + str(age) + ' years old.\n'

    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(fg='snow', bg='hotpink', width=300)

btn = Button(text='Calculate', fg='dark green', bg='khaki', command=display, height=1, width=10)

label1.place(x=20, y=20)
name_entry.place(x=150, y=20)

label2.place(x=20, y=50)
date_entry.place(x=150, y=50)

label3.place(x=20, y=80)
month_entry.place(x=150, y=80)

label4.place(x=20, y=110)
year_entry.place(x=150, y=110)

btn.place(x=170, y=140)

textbox.place(y=180)

root.mainloop()
