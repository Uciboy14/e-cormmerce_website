import os
import sys

sys.path.append('/data/data/com.termux/files/home/storage/shared/anoda/')
from app import app, db
from datetime import datetime
from app.products.models.brand import Brand
from app.products.models.category import Category

from flask_sqlalchemy import SQLAlchemy

class Product(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}  #
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    # Define the foreign key relationship to the 'brands' table
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    brand = db.relationship('Brand', backref='products')
    
    # Define the foreign key relationship to the 'categories' table
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref='products')

    image_1 = db.Column(db.String(256), nullable=False, default='image1.jpg')

    def __repr__(self):
        return '<Product %r>' % self.name

with app.app_context():
  db.create_all()
  db.session.commit()
