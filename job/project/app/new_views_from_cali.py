#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm  # Import your form class
from urllib.parse import quote_plus

ajitkhdm1 = Flask(__name__)
ajitkhdm1.config[
    'SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://zak:{quote_plus("123456")}@zak/calimero'
ajitkhdm1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ajitkhdm1.config['SECRET_KEY'] = '2132'
db = SQLAlchemy(ajitkhdm1)


@ajitkhdm1.route("/")
def homepage():
    return render_template("HOME_PAGE.html", )


@ajitkhdm1.route("/contact")
def contact():
    return render_template("contact.html")


@ajitkhdm1.route("/prive")
def sctr_prv():
    return render_template("sctr_prv.html", pp="PRIVé")


@ajitkhdm1.route("/public")
def sctr_pblc():
    return render_template("sctr_pblc.html", pp="public")


@ajitkhdm1.route("/councours")
def councours():
    return render_template('modls_councours.html',  pp="councours")


@ajitkhdm1.route("/stages")
def stages():
    return render_template('stages.html', pp=" stages")


@ajitkhdm1.route("/orientation")
def orientation():
    return render_template("orientation.html", pp="oriontations")


@ajitkhdm1.route("/faq")
def faq():
    return render_template("faq_page.html", pp="faq")


@ajitkhdm1.route("/404")
def notf():
    return ("THIS PAGE NOT FOUND")


@ajitkhdm1.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()  # Replace with the actual form class
    if request.method == 'POST' and form.validate_on_submit():
        # Process the form data
        username = form.username.data
        # Insert data into the database
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html', form=form)


@ajitkhdm1.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Replace with the actual form class
    if request.method == 'POST' and form.validate_on_submit():
        # Process the form data
        username = form.username.data
        # Insert data into the database
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('login.html', form=form)

if __name__ == "__main__":
    ajitkhdm1.run(debug=True, port=9000)
