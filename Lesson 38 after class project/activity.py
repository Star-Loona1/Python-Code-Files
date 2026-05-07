from tkinter import *

root = Tk()
root.title('Length converter App')
root.geometry('400x400')

label1 = Label(text="Let's convert inches to centimetres", fg='snow', bg='rebeccapurple', height=1, width=50)

label2 = Label(text='INPUT THE NUMBER OF INCHES', fg='lavender', bg='olivedrab', height=1, width=50)

entry_inches = Entry(fg='midnightblue', bg='dark khaki', width=15)

def display():
    inches = float(entry_inches.get())
    cm = inches*2.54
    message = str(inches) + ' inches is equal to ' + str(cm) + ' centimetres.\n'

    textbox.insert(END, message)

textbox = Text(fg='snow', bg='hotpink', width=60)

btn = Button(text='Convert', fg='tomato', bg='khaki', command=display, height=1, width=10)

label1.place(x=20, y=0)
label2.place(x=20, y=20)
entry_inches.place(x=140, y=50)
btn.place(x=150, y=80)
textbox.place(y=130)

root.mainloop()
