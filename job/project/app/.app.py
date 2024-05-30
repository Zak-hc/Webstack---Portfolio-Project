#!/usr/bin/python3
from flask import Flask, render_template
from forms import RegistrationForm

ajitkhdm1 = Flask(__name__)
ajitkhdm1.config['SECRET_KEY'] = '2132'
@ajitkhdm1.route("/")
def homepage():
    return render_template("HOME_PAGE.html")

@ajitkhdm1.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html",form=form)

if __name__ == "__main__":
    ajitkhdm1.run(debug=True)

