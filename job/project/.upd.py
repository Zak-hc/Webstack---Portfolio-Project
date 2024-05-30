#!/usr/bin/python3
from flask import Flask
from app import db
from app.models import User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    # Trouver l'utilisateur avec l'email spécifié
    user_to_update = User.query.filter_by(email='admin@example.com').first()

    # Mettre à jour la colonne is_admin
    if user_to_update:
        user_to_update.is_admin = True
        db.session.commit()

