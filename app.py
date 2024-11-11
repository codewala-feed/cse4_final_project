from flask import Flask, render_template, request, redirect
from pymongo import MongoClient


app = Flask(__name__)
my_connection = MongoClient("localhost", 27017)
my_db = my_connection["cse4_final"]
students = my_db["students"]
callme = my_db["callme"]


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/callme", methods=["GET", "POST"])
def callme_details():
    name = request.form["name"]
    email = request.form["email"]
    number = request.form["number"]
    course = request.form["course"]
    callme.insert_one(
        {"name":name, "email":email, "number":number, "course":course}
    )
    return redirect("/")


@app.route("/admissions", methods=["GET"])
def admissions():
    return render_template("admissions.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        _id = request.form["id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        percentage = request.form["percentage"]
        rank = request.form["rank"]
        course = request.form["course"]
        address = request.form["address"]
        return "Registered Successfully"
    else:
        return render_template("register.html")

@app.route("/view", methods=["GET"])
def view():
    return render_template("view.html")

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        _id = request.form["id"]
        new_field = request.form["new_field"]
        new_value = request.form["new_value"]
        return "Updated Successfully"
    else:
        return render_template("update.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        _id = request.form["id"]
        return "Deleted Successfully"
    else:
        return render_template("delete.html")

@app.route("/campus_tour", methods=["GET", "POST"])
def campus_tour():
    return render_template("campus_tour.html")

app.run(debug=True)