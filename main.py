from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), unique=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), unique=True, nullable=False)
    description = db.Column(db.String(length=1024), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name}'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

