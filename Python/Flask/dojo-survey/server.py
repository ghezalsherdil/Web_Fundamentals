from flask import Flask, render_template, request, redirect
app = Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey', methods=["POST"])
def survey():
    print "Got Post Info"
    return request.form['name']
    return request.form['location']
    return request.form['rows']
    return "got data"
    return redirect('/survey')

app.run(debug=True)
