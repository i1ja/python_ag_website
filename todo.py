from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

todos=["test1","test2"]
@app.route("/")
def todo():
    return render_template("todo.html", todos=todos)

@app.route("/add")
def add():
    todos.append(request.args["todo"])
    return redirect(url_for('todo'))

app.run(debug=True)