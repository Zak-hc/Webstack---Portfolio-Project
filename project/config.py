#!/usr/bin/python3
# config.py dont tuch this configuration please
import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://admin:{quote_plus("123456")}@localhost/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
