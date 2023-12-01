from tkinter import *
import random, string


root = Tk()
root.geometry("500x300")
root.title("Ayush.com - Strong Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("The strength of our password:")
root.iconbitmap('E:\my games and Etc\FALKEN GAMING\BACKROUND\logos_pics\F (2).ico')



def selection():
        selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()


lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

#
val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

# passprint


def callback():
        lsum.config(text=passgen())


        # clickable button
passgenButton = Button(root, text="Generate Password", bd=7, height=2, command=callback, padx=50,pady=13)
passgenButton.pack()    
password = str(callback)

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols


def passgen():
        if choice.get() == 1:
                return "".join(random.sample(poor, val.get()))
        elif choice.get() == 2:
                return "".join(random.sample(average, val.get()))
        elif choice.get() == 3:
                return "".join(random.sample(advance, val.get()))


root.mainloop()