from flask import Flask, render_template, request, redirect, session
from random import randint
import datetime

app = Flask(__name__)
gold = 0
activities = []
@app.route('/')
def index():
    return render_template("index.html", gold=gold, activities=activities)

@app.route('/process_money', methods=["POST"])
def process_money():
    global gold
    if request.form['Building'] == "Farm":
        earned=randint(10, 20)
        gold = gold + earned
        activities.append ("<span class='green'>Earned " + str(earned) + " golds from the " + request.form['Building'] + "! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "</span>")
    elif request.form['Building'] == "Cave":
        earned=randint(5, 10)
        gold = gold + earned
        activities.append ("<span class='green'>Earned " + str(earned) + " golds from the " + request.form['Building'] + "! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "</span>")
    elif request.form['Building'] == "House":
        earned=randint(2, 5)
        gold = gold + earned
        activities.append ( "<span class='green'>Earned " + str(earned) + " golds from the " + request.form['Building'] + "! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "</span>")
    elif request.form['Building'] == "Casino":
        earned=randint(-50, 50)
        gold = gold + earned
        if earned<0:
            activities.append ("<span class='red'>Entered a casino and lost " + str(earned) + " golds..." + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "</span>")
        else:
            activities.append ("<span class='green'>Earned " + str(earned) + " golds from the " + request.form['Building'] + "! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M" )+ "</span>")

    print activities
    return redirect('/')


app.run(debug=True)
