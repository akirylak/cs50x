import os

from cs50 import SQL
from flask import Flask, render_template, flash, redirect, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

app = Flask(__name__)



app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database

db = SQL("sqlite:///sqldata.db")

#index page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/links')
def links():
    return render_template("links.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/connect')
def connect():
    return render_template("connect.html")

@app.route('/form', methods=["GET", "POST"])
def form():
    if (request.method == "POST"):
        # Step 1: username and password from register.html
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        linkedin = request.form.get('linkedin')
               # Step 3: not statements for error checking if information was entered in form field
        if not firstname:
            return render_template("oops.html")
        elif not lastname:
            return render_template("oops.html")
        elif not email:
            return render_template("oops.html")
        db.execute("INSERT INTO connect (lastname, firstname, email, linkedin) VALUES(?, ?, ?, ?)", lastname, firstname, email, linkedin)

    return render_template("thankyou.html")

