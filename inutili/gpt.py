import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Ac-Milan"
)


conn.commit()

conn.close()


