from flask import Flask, render_template, request, redirect
app = Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test', methods=["POST"])

def survey():
    print "Got Post Info"
    print request.form['name']
    print request.form['location']
    print request.form['rows']
    return "got data"
    return redirect('/test')

app.run(debug=True)
