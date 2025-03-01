from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Ac_Milan"
)
mycursor = mydb.cursor()


app = Flask(__name__)


@app.route("/Ac_Milan")
def unitList():
    mycursor.execute("SELECT * FROM Calciatori_Milan")
    myresult = mycursor.fetchall()
    return render_template('calciatori.html', players=myresult)

@app.route('/Cognome/<calciatore>')    
def calcio(calciatore):
    mycursor.execute("SELECT * FROM Calciatori_Milan where Cognome='{}'".format(calciatore))
    myresult = mycursor.fetchall()
    return render_template('cognome.html', tabella_calciatori=myresult)
