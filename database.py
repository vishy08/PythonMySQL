from tkinter import *
from tkinter import messagebox
import mysql.connector

#myCursor.execute("CREATE DATABASE testdb")
#myCursor.execute("SHOW DATABASES")

#for i in myCursor:
#    print(i[0])

#myCursor.execute("CREATE TABLE users (firstName VARCHAR(255), middleInitial VARCHAR(5), lastName VARCHAR(255), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")


# function to delete record
def delete():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rear7sub",
    database = "testdb")

    myCursor = mydb.cursor()

    # Delete the record
    myCursor.execute("DELETE from users WHERE user_id = " + deleteBox.get())

    messagebox.showinfo("information", "Record deleted successfully...")

    deleteBox.delete(0, END)

    # commit changes
    mydb.commit()

    mydb.close()


# function to add record
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
    mydb.close()

    # Clear text boxes
    textBox1.delete(0, END)
    textBox2.delete(0, END)
    textBox3.delete(0, END)

# Create Query function
def query():
    #root = Tk()
    root.geometry("700x500")
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rear7sub",
    database = "testdb")

    myCursor = mydb.cursor()

    # query the database
    myCursor.execute("SELECT *, user_id FROM users")
    records = myCursor.fetchall()
    print(records)

    # loop through results
    print_records = ''
    for record in records:
        print_records += str(record[3]) + " " + str(record[0]) + " " + str(record[2]) + "\n"

    query_label = Label(root, text=print_records)
    #.pack(side=TOP, anchor="e")
    #query_label.grid(row=8, column=5, columnspan=2)
    query_label.place(x=500, y=0)

    # commit changes
    mydb.commit()

    mydb.close()

root = Tk()
root.geometry("350x400")

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

addButton = Button(root, text="Add", command = add, height=3, width=30)
addButton.place(x=10, y=130)

deleteBox = Entry(root)
deleteBox.grid(row=9, column=1)
deleteBox.place(x=140, y=250)

deleteBoxLabel = Label(root, text="ID Number")
deleteBoxLabel.grid(row=9, column=0)
deleteBoxLabel.place(x=10, y=250)

# Create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)
query_btn.place(x=10, y=215)

# create a delete buttons
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)
delete_btn.place(x=10, y=275)

root.mainloop()