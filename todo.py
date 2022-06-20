from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text)


@app.route("/")
def todo():
    print(todos.query.all())
    return render_template("todo.html", todos=todos.query.all())

@app.route("/add")
def add():
    #todos.append(request.args["todo"])
    db.session.add(todos(todo=request.args["todo"]))
    db.session.commit()
    return redirect(url_for('todo'))

@app.route("/delete")
def delete():
    db.session.delete(todos.query.get(int(request.args["id"])))
    db.session.commit()
    return redirect(url_for('todo'))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)