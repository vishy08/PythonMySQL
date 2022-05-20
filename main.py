from tkinter import *
import mysql.connector

root = Tk()
root.geometry("800x500")

firstNameLabel = Label(root, text="First Name")
firstNameLabel.place(x=10,y=10)

middleILabel = Label(root, text="Middle Initial")
middleILabel.place(x=10, y=40)

lastNameLabel = Label(root, text="Last Name")
lastNameLabel.place(x=10, y=70)

textBox1 = Entry(root)
textBox1.place(x=140, y=10)

textBox2 = Entry(root)
textBox2.place(x=140, y=40)

textBox3 = Entry(root)
textBox3.place(x=140, y=70)

addButton = Button(root, text="Add", height=3, width=13)
addButton.place(x=140, y=130)


root.mainloop()

#Create connection to database
