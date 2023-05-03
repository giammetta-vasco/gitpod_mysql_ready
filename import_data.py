import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Ac_Milan")

mycursor.execute("DROP  TABLE IF  EXISTS Ac_Milan.Calciatori_Milan")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS Ac_Milan.Calciatori_Milan (
    Cognome VARCHAR(30) NOT NULL,
    Nome VARCHAR(30) NOT NULL,
    Ruolo VARCHAR(30) NOT NULL,
    Numero INTEGER,
    Gol_segnati INTEGER,
    Assist INTEGER,
    Valore VARCHAR(30),
    Eta INTEGER,
    Nazionalita VARCHAR(30) NOT NULL
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM Ac_Milan.Calciatori_Milan")
mydb.commit()

#Read data from a csv file
clash_data = pd.read_csv('./Calciatori_Milan.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO Ac_Milan.Calciatori_Milan VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM Ac_Milan.Calciatori_Milan")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)