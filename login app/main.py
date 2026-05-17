from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#d0efff')

lbl1 = Label(master=frame, text='Full Name', bg='#3895D3', width=12)
lbl2 = Label(master=frame, text='Email Id', bg='#3895D3', width =12)
lbl3 = Label(master=frame, text=' Enter Password', bg='#3895D3', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show='*')

def display():
    name = name_entry.get()
    greet = "Hey" +name
    message = "\nCongratulations for your new account!"
    textbox.insert(END, greet + message)

textbox = Text(bg="#BEBEBE", FG="black")
btn =Button(text = "Create Account", bg="red", command=display)

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=60)
email_entry.place(x=150, y=60)
lbl3.place(x=20, y=100)
password_entry.place(x=150, y=100)
btn.place(x=150, y=140)
textbox.place(x=20, y=180)

root.mainloop()