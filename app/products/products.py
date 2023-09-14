import sys

sys.path.append('/Users/David/Downloads/ANODA/anoda')

from flask import Flask, Blueprint, redirect, url_for, request, flash, render_template, session, current_app
from app import db, app
from app.products.models.product import Product
from app.products.models.brand import Brand
from app.products.models.category import Category
import secrets, os

product_bp = Blueprint('product', __name__,
template_folder='templates',
static_folder='static')

def get_all_brands():
    brands = Brand.query.join(Product, (Brand.id==Product.brand_id)).all()
    return brands

def get_all_categories():
    return Category.query.join(Product, (Category.id==Product.category_id)).all()

@product_bp.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    products = Product.query.filter(Product.stock > 0).paginate(page=page, per_page=4)
    product = Product.query.all()
    print(product)
    return render_template('index.html', title="Store Home", product=product, brands=get_all_brands(), categories=get_all_categories())

@product_bp.route('/cart')
def cart():
  return render_template('cart.html')
  
@product_bp.route('/product/<int:id>')
def product_details(id):
    product = Product.query.get_or_404(id)
    brands = Brand.query.join(Product, (Brand.id==Product.brand_id)).all()
    categories = Category.query.join(Product, (Category.id==Product.category_id)).all()
    return render_template('products/product_details.html', product=product, title=product.name, brands=brands, categories=get_all_categories())

@product_bp.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page', 1, type=int)
    get_b = Brand.query.filter_by(id=id).first_or_404()
    brand = Product.query.filter_by(brand = get_b).paginate(page=page, per_page=4)
    return render_template('products/index.html', brand=brand, title=Brand.query.get(id).name, brands=get_all_brands(), 
    categories=get_all_categories(), get_b=get_b)

@product_bp.route('/category/<int:id>')
def get_category(id):
    page = request.args.get('page', 1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    category = Product.query.filter_by(category = get_cat).paginate(page=page, per_page=4)
    return render_template('products/index.html', category=category, title=Category.query.get(id).name, 
                            categories=get_all_categories(), brands=get_all_brands(), get_cat=get_cat)
