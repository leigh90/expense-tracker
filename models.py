from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
# from flask_alembic import Alembic
app = Flask(__name__)
DB_URI = config('SQLALCHEMY_DATABASE_URI')
# app.debug = True
# app =  SQLAlchemy(app)
db = SQLAlchemy(app)


# alembic = Alembic()
# alembic.init_app(app)

class Expense(db.Model):
    __tablename__ = "expenses"
    id = db.Column(db.Integer, primary_key=True)
    amount_spent = db.Integer(db.String(120), unique=True, nullable=False) #this doesn't need to be unique
    item = db.Integer(db.String(120), unique=True, nullable=False) # How do you fill this?
    payee = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.Date,nullable=False)
    time = db.Column(db.Time, nullable=False)
    transaction_cost = db.Column(db.Integer, nullable=True)
    category_name = db.Column(db.String(50), db.ForeignKey('category.name'), nullable=True)

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.relationship("Expense",backref = 'Category')

