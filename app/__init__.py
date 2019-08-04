from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
 
from app.alarm.views import alarmsList
app.register_blueprint(alarmsList)
 
db.create_all()