from flask import Flask
from zeep import Client
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


import sys
sys.path.append(".")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/namedb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your secret key'

from celular.controllers.celularController import  Route
app.register_blueprint(Route, url_prefix='/')
