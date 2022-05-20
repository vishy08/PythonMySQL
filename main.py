import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")
myCursor = mydb.cursor()
myCursor.execute("show databases")

for i in myCursor:
    print(i)