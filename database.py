from tkinter import *
from tkinter import messagebox
import mysql.connector

#myCursor.execute("CREATE DATABASE testdb")
#myCursor.execute("SHOW DATABASES")

#for i in myCursor:
#    print(i[0])

#myCursor.execute("CREATE TABLE users (firstName VARCHAR(255), middleInitial VARCHAR(5), lastName VARCHAR(255), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

# Create edit function to update record
def edit():
    global editor
    editor = Tk()
    editor.title("Editor")
    editor.geometry("350x400")

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rear7sub",
    database = "testdb")

    myCursor = mydb.cursor()

    record_id = deleteBox.get()

    # query the database
    myCursor.execute("SELECT * FROM users WHERE user_id = " + record_id)
    records = myCursor.fetchall()

    global textBox1_editor
    global textBox2_editor
    global textBox3_editor

    firstNameLabel = Label(editor, text="First Name")
    firstNameLabel.place(x=10,y=10)

    middleILabel = Label(editor, text="Middle Initial")
    middleILabel.place(x=10, y=40)

    lastNameLabel = Label(editor, text="Last Name")
    lastNameLabel.place(x=10, y=70)

    textBox1_editor = Entry(editor)
    textBox1_editor.place(x=140, y=10)

    textBox2_editor = Entry(editor)
    textBox2_editor.place(x=140, y=40)

    textBox3_editor = Entry(editor)
    textBox3_editor.place(x=140, y=70)

    for record in records:
        textBox1_editor.insert(0, record[0])
        textBox2_editor.insert(0, record[1])
        textBox3_editor.insert(0, record[2])

    # create an save button
    save_btn = Button(editor, text="Save Record", command=save, height=3, width=30)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)
    save_btn.place(x=10, y=130)


    mydb.commit()
    mydb.close()


    # function to save edited record
def save():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rear7sub",
    database = "testdb")

    myCursor = mydb.cursor()

    firstName = textBox1_editor.get()
    middleInitial = textBox2_editor.get()
    lastName = textBox3_editor.get()
    record_id = deleteBox.get()

    #myCursor.execute("""
    #UPDATE users
    #SET
    #    firstName = :'first',
    #    middleInitial = ':middle',
    #    lastName = ':last'

           # WHERE user_id = """ + record_id,
        #{
        #'first': textBox1_editor.get(),
        #'middle': textBox2_editor.get(),
        #'last': textBox3_editor.get(),
        ##'user_id': record_id
        #})

    myCursor.execute("UPDATE users SET firstName = '" + firstName + "' WHERE user_id = " + record_id)
    #val = (firstName, middleInitial, lastName)
    #myCursor.execute(sqlStuff, val)

    mydb.commit()
    mydb.close()


    

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
root.title("Vishy's Patient Index Database Form")
root.geometry("350x400")

global textBox1
global textBox2
global textBox3
global deleteBox

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

deleteBoxLabel = Label(root, text="Select ID")
deleteBoxLabel.grid(row=9, column=0)
deleteBoxLabel.place(x=10, y=250)

# Create a query button
query_btn = Button(root, text="Show Records", command=query, height=2, width=20)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)
query_btn.place(x=55, y=200)

# create a delete buttons
delete_btn = Button(root, text="Delete Record", command=delete, height=2, width=20)
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)
delete_btn.place(x=55, y=290)

# create an update button
update_btn = Button(root, text="Update Record", command=edit, height=2, width=20)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)
update_btn.place(x=55, y=340)

root.mainloop()