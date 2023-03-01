import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

cursor = conn.cursor()

query = "INSERT INTO Mammiferi (name, specie) VALUES (%s, %s)"
valori = [
  ('Cane', 'Canide'),
  ('Gatto', 'Felide'),
  ('Leone', 'Felide'),
  ('Orso', 'Urside'),
  ('Tigre', 'Felide')
]
cursor.executemany(query, valori)

conn.commit()

conn.close()


