from flask import Flask, render_template
app = Flask(__name__)

skills=["python","html ;)"]
@app.route("/")
def ilja():
    return render_template("ilja.html", skills=skills)



app.run(debug=True)