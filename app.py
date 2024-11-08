from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/callme", methods=["GET", "POST"])
def callme_details():
    name = request.form["name"]
    email = request.form["email"]
    number = request.form["number"]
    course = request.form["course"]
    return "Call Requested"


@app.route("/admissions", methods=["GET"])
def admissions():
    return render_template("admissions.html")

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/view", methods=["GET"])
def view():
    return render_template("view.html")

@app.route("/update", methods=["GET"])
def update():
    return render_template("update.html")

@app.route("/delete", methods=["GET"])
def delete():
    return render_template("delete.html")

@app.route("/campus_tour", methods=["GET"])
def campus_tour():
    return render_template("campus_tour.html")

app.run(debug=True)