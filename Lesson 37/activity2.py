from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, bg='teal', height=300, width=360)

label1 = Label(frame, text='Full name', fg='white', bg='navy', width=12)
label2 = Label(frame, text='Email Id', fg='snow', bg='dark orchid', width=12)
label3 = Label(frame, text='Password', fg='white', bg='cadetblue', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show='*')

def display():
    name = name_entry.get()
    greet = 'Hello, ' + name + '.\n'

    message = 'Your account has been successfully created.\n'

    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(fg='black', bg='grey')

btn = Button(text='Create account', fg='saddlebrown', bg='lavender', command=display, height=1, width=10)

frame.place(x=20, y=0)
label1.place(x=20, y=20)
name_entry.place(x=150, y=20)

label2.place(x=20, y=80)
email_entry.place(x=150, y=80)

label3.place(x=20, y=140)
pass_entry.place(x=150, y=140)

btn.place(x=130, y=210)

textbox.place(y=250)

root.mainloop()
