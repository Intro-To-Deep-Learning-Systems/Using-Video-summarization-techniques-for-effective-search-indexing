import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root1234",
  database="searchindex"

)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE searchindex")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
# print(mydb)

mycursor.execute("CREATE TABLE searchkeywords (link VARCHAR(10000), keywords VARCHAR(10000))")