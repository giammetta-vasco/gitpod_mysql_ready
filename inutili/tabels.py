import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Ac Milan"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (name VARCHAR(255), specie VARCHAR(255))")