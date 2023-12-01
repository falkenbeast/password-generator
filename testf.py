from tkinter import *
from random import randint

root = Tk()
root.title('Ayush.com - Strong Password Generator')
root.iconbitmap('E:\my games and Etc\FALKEN GAMING\BACKROUND\logos_pics\F (2).ico')
root.geometry("500x300")



#my_password = chr(randint(33,126))

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





def clipper():
    root.clipboard_clear() 

    root.clipboard_append(pw_entry.get())

lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

# af = LabelFrame(root, text="Enter Special Feature Want to include")
# af.pack(pady=20)



my_entry = Entry(lf, font=("Helvetica", 24)) 
my_entry.pack(pady=20,  padx=20)




pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)


my_frame = Frame(root)
my_frame.pack(pady=20)


my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)


clip_button = Button(my_frame, text="Copy To Clipboad", command=clipper)
clip_button.grid(row=0, column=1, padx=10)
root.mainloop()
