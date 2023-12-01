from tkinter import *
import string
import random
import pyperclip


def generator():
    passwordField.delete(0, END)
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(numbers+capital_alphabets+small_alphabets,password_length))

    if choice.get()==4:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg= '#1F1F1F')
root.title('Ayush.com - Strong Password Generator')
root.iconbitmap('E:\my games and Etc\FALKEN GAMING\BACKROUND\logos_pics\F (2).ico')
choice=IntVar()

Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='#1F1F1F',fg='white')
passwordLabel.grid(padx=250,pady=20)

weakradioButton=Radiobutton(root,text='Small Alphabets',value=1,variable=choice,font=Font, width=21,)
weakradioButton.grid(pady=5, row=20,column= 0)
warnLabel=Label(root,text='⚠️Max Limit 26 characters',font=('times new roman',12,'bold'),bg='#1F1F1F',fg='white')
warnLabel.grid(row=20,column=30,padx=15,pady=15)


mediumradioButton=Radiobutton(root,text='Capital + Small Alphabhets',value=2,variable=choice,font=Font,width=21)
mediumradioButton.grid(pady=5, row=40, column=0)
warnLabel=Label(root,text='⚠️Max Limit 52 characters',font=('times new roman',12,'bold'),bg='#1F1F1F',fg='white')
warnLabel.grid(row=40,column=30,padx=15,pady=15)


numradioButton=Radiobutton(root,text='With Digits',value=3,variable=choice,font=Font, width=21)
numradioButton.grid(pady=5,row=60,column=0)
warnLabel=Label(root,text='⚠️Max Limit 62 characters',font=('times new roman',12,'bold'),bg='#1F1F1F',fg='white')
warnLabel.grid(row=60,column=30,padx=15,pady=15)


strongradioButton=Radiobutton(root,text='With Special Characters',value=4,variable=choice,font=Font,width=21)
strongradioButton.grid(pady=5,row=80,column=0)
warnLabel=Label(root,text='⚠️Max Limit 94 characters',font=('times new roman',12,'bold'),bg='#1F1F1F',fg='white')
warnLabel.grid(row=80,column=30,padx=15,pady=15)


lengthLabel=Label(root,text='Password Length',font=Font,bg='#1F1F1F',fg='white')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator, bd=4)
generateButton.grid(pady=20)

passwordField=Entry(root,width=50,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text='Copy',font=Font,command=copy,bd=4)
copyButton.grid(pady=5)


root.mainloop()

