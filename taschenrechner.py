from flask import Flask

app = Flask(__name__)

@app.route("/<nummer1>/plus/<nummer2>")
def plus(nummer1,nummer2):
    nummer3=int(nummer1)+int(nummer2)
    return "das ergebis ist: "+str(nummer3)
@app.route("/<nummer1>/minus/<nummer2>")
def minus(nummer1,nummer2):
    nummer3=int(nummer1)-int(nummer2)
    return "das ergebis ist: "+str(nummer3)
@app.route("/<nummer1>/mal/<nummer2>")
def mal(nummer1,nummer2):
    nummer3=int(nummer1)*int(nummer2)
    return "das ergebis ist: "+str(nummer3)
@app.route("/<nummer1>/durch/<nummer2>")
def geteilt(nummer1,nummer2):
    nummer3=int(nummer1)/int(nummer2)
    return "das ergebis ist: "+str(nummer3)

app.run(debug=True)