from tkinter import *
from tkinter import messagebox
import mysql.connector

#myCursor.execute("CREATE DATABASE testdb")
#myCursor.execute("SHOW DATABASES")

#for i in myCursor:
#    print(i[0])

#myCursor.execute("CREATE TABLE users (firstName VARCHAR(255), middleInitial VARCHAR(5), lastName VARCHAR(255), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")


def add():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rear7sub",
    database = "testdb")

    myCursor = mydb.cursor()
    
    firstName = textBox1.get()
    middleInitial = textBox2.get()
    lastName = textBox3.get()

    sqlStuff = "INSERT INTO users (firstName, middleInitial, lastName) VALUES (%s, %s, %s)"
    val = (firstName, middleInitial, lastName)
    myCursor.execute(sqlStuff, val)
    mydb.commit()
    #lastid = myCursor.lastrowid
    messagebox.showinfo("information", "Record inserted successfully...")

root = Tk()
root.geometry("800x500")

global textBox1
global textBox2
global textBox3

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

addButton = Button(root, text="Add", command = add, height=3, width=13)
addButton.place(x=140, y=130)


root.mainloop()