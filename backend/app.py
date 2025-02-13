from flask import Flask, request, url_for, redirect, render_template
from flask_restful import Api, Resource
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import declarative_base
from import_files.models import db, User, Item, Bill, Bill_Items


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addItem', methods=['GET','POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add-item.html')
    else:
        name = request.form.get("name")
        w_price = request.form.get("w_price")
        r_price = request.form.get("r_price")
        stock = request.form.get("stock")
        description = request.form.get("description")
        item = Item(name=name, w_price=w_price, r_price=r_price, stock=stock, description=description)
        db.session.add(item)
        db.session.commit()
        return render_template('add-item.html', message="Item added successfully")
        


if __name__ == '__main__':
    # app.run(debug=True)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
