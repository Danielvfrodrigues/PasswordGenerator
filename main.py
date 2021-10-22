from tkinter import *
import tkinter.messagebox
from random import randint, choice

root = Tk()
root.title('Password Generator')
# root.iconbitmap('logo2.ico')
root.geometry("500x350")

# uppercase = chr(randint(41, 90))
# lowercase = chr(randint(97, 122))
# numbers = chr(randint(48, 57))
# symbols = chr(randint(33, 47))
# all_chars = chr(randint(33, 126))


# Generate random strong password


def new_rand():
    # Clear the entry box
    pw_entry.delete(0, 'end')

    # Get the pw legnth and conver to int
    pw_length = int(my_entry.get())

    # Create variable to hold the pw

    symbols = ['!', '@', '#', '$', '%', '&', '*', '-', '=', '+', '.', '/']
    my_chars = []
    my_password = ''

    # Loop through password length
    if Checkbutton1.get() == 1:
        for x in range(pw_length):
            my_chars.append(chr(randint(65, 90)))

    if Checkbutton2.get() == 1:
        for x in range(pw_length):
            my_chars.append(chr(randint(97, 122)))

    if Checkbutton3.get() == 1:
        for x in range(pw_length):
            my_chars.append(chr(randint(48, 57)))

    if Checkbutton4.get() == 1:
        for x in range(pw_length):
            my_chars.append(choice(symbols))

    for i in range(pw_length):
        my_password += choice(my_chars)
    pw_entry.insert(0, my_password)

# Copy to clipboard


def clipper():
    # Clear the clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())
    tkinter.messagebox.showinfo(
        title="Password Generator", message="Copied to Clipboard")


# Label Frame
lf = LabelFrame(root, text="Password Length")
lf.pack(pady=20)

# Create Entry Box to designate number of characters
my_entry = Spinbox(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

# Create Entry Box for our returned password
pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

# Create a frame for the buttons
btn_frame = Frame(root)
btn_frame.pack(pady=(20, 15))

# Create a frame for the checkboxes
box_frame = Frame(root)
box_frame.pack(pady=5)


# Create checkboxes to define the characters
Checkbutton1 = IntVar()
cb_upper = Checkbutton(box_frame, text='Uppercase', font=("Helvetica", 10),
                       variable=Checkbutton1).grid(row=0, column=1)

Checkbutton2 = IntVar()
cb_lower = Checkbutton(box_frame, text='Lowercase', font=("Helvetica", 10),
                       variable=Checkbutton2).grid(row=0, column=2)

Checkbutton3 = IntVar()
cb_number = Checkbutton(box_frame, text='Numbers', font=("Helvetica", 10),
                        variable=Checkbutton3).grid(row=0, column=3)

Checkbutton4 = IntVar()
cb_symbol = Checkbutton(box_frame, text='Symbols', font=("Helvetica", 10),
                        variable=Checkbutton4).grid(row=0, column=4)

# Create the buttons
my_button = Button(btn_frame, text="Generate Strong Password",
                   command=new_rand)
my_button.grid(row=1, column=0, padx=10)

# Create Copy to clipboard button
clip_button = Button(btn_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=1, column=1, padx=10)

root.mainloop()
