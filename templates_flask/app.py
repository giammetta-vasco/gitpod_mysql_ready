# save this as hello.py
from flask import Flask


app = Flask(__name__)


@app.route("/Ac_Milan")
def unitList():
    mycursore.execute(SELECT * FROM Ac_Milan)
    myresult = mycursor.fetchall()
    return rendern_template('calciatori.html', units=myresult)