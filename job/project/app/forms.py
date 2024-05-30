#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])    
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    signup = SubmitField('Sign Up')
    signin = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    remember = BooleanField("remember me !")
    signup = SubmitField('Sign Up')
    signin = SubmitField('Sign In')
    is_admin = BooleanField('Is Admin') # Cette ligne reste pour l'inscription, elle sera masquée pour les utilisateurs normaux

class Modifinfo(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Modifier')
