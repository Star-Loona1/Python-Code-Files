# 1) Import required modules:
#    a) Import everything from `tkinter` to build the GUI.
#    b) Import `askopenfilename` and `asksaveasfilename` from `tkinter.filedialog`
#       to open and save files using dialog boxes.

# 2) Create the main window using `window = Tk()`.

# 3) Set window properties:
#    a) Set the title to "Codingal's Text Editor".
#    b) Set the window size to 600x500.
#    c) Configure the grid layout (rows and columns) so the editor can expand.

# 4) Define a function `open_file()` to open a text file:
#    a) Use `askopenfilename()` to let the user select a file.
#    b) If no file is selected, return from the function.
#    c) Clear the existing text in the editor using `txt_edit.delete(1.0, END)`.
#    d) Open the selected file in read mode.
#    e) Read the file contents and store them in `text`.
#    f) Insert the file contents into the text editor using `txt_edit.insert(END, text)`.
#    g) Update the window title to show the opened file path.

# 5) Define a function `save_file()` to save the text as a new file:
#    a) Use `asksaveasfilename()` to ask the user where to save the file.
#    b) If no save location is selected, return from the function.
#    c) Open the selected path in write mode.
#    d) Get the current content from the text editor using `txt_edit.get(1.0, END)`.
#    e) Write this content into the file.
#    f) Update the window title to show the saved file path.

# 6) Create widgets for the application:
#    a) Create a `Text` widget `txt_edit` for editing text.
#    b) Create a `Frame` `fr_buttons` to hold buttons.
#    c) Create an "Open" button that calls `open_file()`.
#    d) Create a "Save As..." button that calls `save_file()`.

# 7) Arrange widgets using the grid system:
#    a) Place "Open" and "Save As..." buttons inside the frame.
#    b) Place the button frame in the left column.
#    c) Place the text editor in the right column and allow it to expand.

# 8) Start the GUI event loop using `window.mainloop()`
#    so the text editor window remains open and responds to user actions.

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.title("Codingal's Text Editor")
window.geometry('600x500')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    filepath = askopenfilename(
        filetypes = [('Text files', '*.txt'), ('All files', '*.*')]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title("Codingal's Text Editor")

def save_file():
    defaultextension = 'txt'
    filepath = asksaveasfilename(
        filetypes = [('Text Files', '.txt'), ('All files', '*.*')]
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title("Codingal's Text Editor")

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text='Open', command=open_file)
btn_save = Button(fr_buttons, text='Save As....', command=save_file)

btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=0, column=1, sticky='ew', padx=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=1, column=0, sticky='nsew')

window.mainloop()