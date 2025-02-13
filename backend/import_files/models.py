from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    mobile = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    r_price = db.Column(db.Float, unique=False, nullable=False)
    w_price = db.Column(db.Float, unique=False, nullable=False)
    stock = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name

class Bill(db.Model):
    bill_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return '<Bill %r>' % self.id

class Bill_Items(db.Model):
    
    bill_id = db.Column(db.Integer, db.ForeignKey('bill.bill_id'), primary_key=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    # total = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<Bill_Items %r>' % self.id
