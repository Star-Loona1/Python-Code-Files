from tkinter import *

window = Tk()
window.title("Getting started with widgets")
window.geometry('400x300')

label1 = Label(text='We are taking two numbers as input and multplying them', fg='white', bg='teal', height=1, width=300)

label2 = Label(text='Enter the first number in the first textbox', fg='snow', bg='navy', height=1, width=300)
entry1 = Entry(fg='black', bg='grey', width=50)

label3 = Label(text='Enter the sceond number in the first textbox', fg='snow', bg='navy', height=1, width=300)
entry2 = Entry(fg='black', bg='grey', width=50)

def display():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    product = num1*num2
    
    global product_str
    product_str = 'The product is ' + str(product) + ' '

    text_box.insert(END, product_str)

text_box = Text(height=3)

btn = Button(text='Calculate', fg='rosybrown', bg='khaki', command=display, height=1, width=5)

label1.pack()
label2.pack()
entry1.pack()
label3.pack()
entry2.pack()
btn.pack()
text_box.pack()

window.mainloop()
