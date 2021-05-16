import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="colors"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM colors")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
time.sleep(10)