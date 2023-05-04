from flask import rendern_template
from flask import Flask
import nysql.connector


app = Flask(__name__)


@app.route("/Ac_Milan")
def unitList():
    mycursore.execute(SELECT * FROM Ac_Milan)
    myresult = mycursor.fetchall()
    return rendern_template('calciatori.html', units=myresult)


