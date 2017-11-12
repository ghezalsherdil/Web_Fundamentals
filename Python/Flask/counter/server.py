from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
times = 0
@app.route('/')
def index():
	global times
	times = times + 1
	return render_template("index.html", counter=times)

@app.route('/ninja',methods=["POST"])
def ninja():
	global times
	times = times + int(request.form['ninja'])
	print request.form['ninja']
   	return redirect('/')

@app.route('/hackers',methods=["POST"])
def hackers():
	global times
	times = 0
   	return redirect('/')
app.run(debug=True)
