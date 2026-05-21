from tkinter import *
window = Tk()
window.title('SIMPLE INTEREST CALCULATOR')
window.geometry('700x600')

l_principle = Label(text='Enter the principle amount', fg='snow', bg='midnightblue', width=50)
l_rate = Label(text='Enter the rate (Already put out of 100)', fg='snow', bg='midnightblue', width=50)
l_time_period = Label(text='Enter the time period (in years)', fg='snow', bg='midnightblue', width=50)

e_principle = Entry(fg='rebeccapurple', bg='lawngreen', width=25)
e_time = Entry(fg='hotpink', bg='teal', width=25)
e_rate = Entry(fg='khaki', bg='rosybrown', width=25)

def display():
    principle = float(e_principle.get())
    time = float(e_time.get())
    rate = float(e_rate.get())
    simple_interest = (principle*time*rate)/100
    compound_interest = principle + simple_interest
    message1 = 'The simple interest is ' + str(simple_interest) + '.\n'
    message2 = 'The compound interest is ' + str(compound_interest) + '.\n'
    textbox1.insert(END, message1)
    textbox2.insert(END, message2)

textbox1 = Text(fg='midnightblue', bg='snow', height=10, width=200)
textbox2 = Text(fg='tomato', bg='dark khaki', height=10, width=200)
btn = Button(text='Calculate', fg='rosybrown', bg='dark khaki', command=display, height=1, width=10)

l_principle.place(x=100, y=0)
e_principle.place(x=200, y=30)
l_rate.place(x=100, y=70)
e_rate.place(x=200, y=110)
l_time_period.place(x=100, y=150)
e_time.place(x=200, y=190)
btn.place(x=250, y=230)
textbox1.place(y=270)
textbox2.place(y=410)

window.mainloop()