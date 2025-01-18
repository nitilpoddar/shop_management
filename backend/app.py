from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db.init_app(app)

class Item(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int] = mapped_column(default=0)
    stock: Mapped[int] = mapped_column(default=0)


@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/add-item', methods=['GET', 'POST'])
def AddProduct():
    if request.method == 'GET':
        itemdata = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
        return render_template("add-item.html", items = itemdata, css_file = 'add-item.css' )
    else:
        # return redirect(url_for("Index"))
        name = request.form.get("name")
        price = request.form.get("price")
        stock = request.form.get("stock")

        newItem = Item(name = name, price = price, stock = stock)
        db.session.add(newItem)
        db.session.commit()
        return redirect(url_for("AddProduct"))
        # return f'the name is {name} and the price is {price} and the stock is {stock} !!!!!!'


@app.route('/inventory')
def Inventory():
    return render_template("index.html")

@app.route('/customer')
def Customer():
    return render_template("index.html")

@app.route('/billing')
def Billing():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(
            debug=True
        )

