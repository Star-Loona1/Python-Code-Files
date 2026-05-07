from tkinter import *
window = Tk()

window.title('Event handler')
window.geometry('100x100')

def handle_keypress(event):
    '''Receives an event object automatically'''
    print(event.char)

window.bind('<Key>', handle_keypress)

def handle_click(event):
    '''Also receives the event object automatically'''
    print('The button is clicked!')

btn = Button(text='Click Me', fg='white', bg='orange', height=10, width=10)
btn.pack()

window.bind('<Button 1>', handle_click)

window.mainloop()