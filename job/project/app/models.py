#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
# from __init__ import app
#from  flask_bcrypt import Bcrypt

db = SQLAlchemy()
#bcrypt = Bcrypt()
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(50), nullable=True)  # 'candidate' or 'employer'
    is_admin = db.Column(db.Boolean, default=False)  # Ajout de la colonne is_admin
 
 #   def set_password(self, password):
   #     self.password = bcrypt.generate_password_hash(password).decode('utf-8')

  #  def check_password(self, password):
  #      return bcrypt.check_password_hash(self.password, password)

class JobCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    industry_id = db.Column(db.Integer)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.DECIMAL)
    publication_date = db.Column(db.Date, default=datetime.utcnow)
    application_deadline = db.Column(db.Date)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    contract_type = db.Column(db.String(50))
    category_id = db.Column(db.Integer, db.ForeignKey('job_category.id'))

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    offer_id = db.Column(db.Integer, db.ForeignKey('job_offer.id'))
    cv = db.Column(db.Text)
    cover_letter = db.Column(db.Text)
    application_date = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.String(50))

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#zid labaqi matzid
