import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rear7sub",
    database = "testdb")

myCursor = mydb.cursor()
#myCursor.execute("CREATE DATABASE testdb")
#myCursor.execute("SHOW DATABASES")

#for i in myCursor:
#    print(i[0])

#myCursor.execute("CREATE TABLE users (firstName VARCHAR(255), middleInitial VARCHAR(5), lastName VARCHAR(255), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

myCursor.execute("SHOW TABLES")
for table in myCursor:
    print(table[0])

sqlStuff = "INSERT INTO users (firstName, middleInitial, lastName) VALUES (%s, %s, %s)"

record1 = ("Vishal", "R", "Kasula")

myCursor.execute(sqlStuff, record1)
mydb.commit()