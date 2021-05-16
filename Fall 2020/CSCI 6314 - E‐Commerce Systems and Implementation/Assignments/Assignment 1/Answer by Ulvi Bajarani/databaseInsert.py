import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="colors"
)

mycursor = mydb.cursor()

sql = "INSERT INTO colors (Name, FavColor) VALUES (%s, %s)"
val = ("John", "green")
mycursor.execute(sql, val)
val = ("John", "blue")
mycursor.execute(sql, val)
val = ("John", "white")
mycursor.execute(sql, val)
val = ("John", "red")
mycursor.execute(sql, val)
val = ("John", "pink")
mycursor.execute(sql, val)

mydb.commit()

print("records were inserted.")
time.sleep(10)