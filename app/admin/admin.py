import sys

#sys.path.append('/data/data/com.termux/files/home/storage/shared/anoda/')

from flask import Flask, Blueprint, render_template, session, request, redirect, url_for, flash
from app import app, db, login_manager
from app.admin.forms.forms import AddProducts

admin_bp = Blueprint('admin', __name__,
    template_folder='templates',
    static_folder='static'
                      )

@login_manager.user_loader
def load_user():
  return None

@admin_bp.route('/addbrand', methods=["GET", "POST"])
def addbrand():
    if request.method == "POST":
        getBrand = request.form.get('brand')
        brand = Brand(name=getBrand)
        db.session.add(brand)
        flash(f'The Brand {getBrand} was added to DataBase.', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add Brand', brands='brands')

@admin_bp.route('/addcategory', methods=["GET", "POST"])
def addcategory():
    if request.method == "POST":
        getCategory = request.form.get('category')
        category = Category(name=getCategory)
        db.session.add(category)
        flash(f'The Category {getCategory} was added to DataBase.', 'success')
        db.session.commit()
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html', title='Add Category')

@admin_bp.route('/addproduct', methods=["GET", "POST"])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddProducts(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        stock = form.stock.data
        desc = form.desc.data
        brand_id = request.form.get('brand')
        category_id = request.form.get('category')
        print(f"Brand ID:{brand_id}, Category Id:{category_id}")
        # category = Category.query.get(id=category_id).first()
        # brand = Brand.query.get(id=brand_id).first()
        # print(f"Brand:{brand}, Category:{category}")
        image_1 = photos.save(request.files['image_1'] , name=secrets.token_hex(10) + '.')
        print(f"Image 1 name:{image_1}, its type:{type(image_1)}")
        product = Product(name=name, price=price, stock=stock, desc=desc, brand_id=brand_id, 
        category_id=category_id, image_1=image_1)
        db.session.add(product)
        flash(f"{name} has been added to database.", 'success')
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('products/addproduct.html', title='Add Product', form=form, brands=brands, 
                            categories=categories)

@admin_bp.route('/updatebrand/<int:id>', methods=["GET", "POST"])
def updatebrand(id):
    if 'email' not in session:
        flash('Please Log In first', 'danger')
    
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == "POST":
        updatebrand.name = brand
        flash(f'Your brand has been updated', 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updatebrand.html', title="Update Brand Info", 
                            updatebrand=updatebrand)

@admin_bp.route('/updatecategory/<int:id>', methods=["GET", "POST"])
def updatecategory(id):
    if 'email' not in session:
        flash('Please Log In first', 'danger')
    
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == "POST":
        updatecategory.name = category
        flash(f'Your category has been updated', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template('products/updatebrand.html', title="Update category Info", 
                            updatecategory=updatecategory)    

@admin_bp.route('/updateproduct/<int:id>', methods=["GET", "POST"])
def updateproduct(id):
    if 'email' not in session:
        flash('Please Log In first', 'danger')
    brands = Brand.query.all()
    categories = Category.query.all()
    brand = request.form.get('brand')
    category = request.form.get('category')
    product = Product.query.get_or_404(id)
    form = AddProducts(request.form)
    if request.method == "POST":
        product.name = form.name.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.desc = form.desc.data
        product.brand_id = brand
        product.category_id = category
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/' + product.image_1))
                product.image_1 = photos.save(request.files['image_1'] , name=secrets.token_hex(10) + '.')
            except:
                product.image_1 = photos.save(request.files['image_1'] , name=secrets.token_hex(10) + '.')
        db.session.commit()
        flash('Product Updated', 'success')
        return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.stock.data = product.stock
    form.desc.data = product.desc
    return render_template('products/updateproduct.html', title="Update Product", form=form, brands=brands,
                        categories=categories, product=product) #, updatebrand=updatebrand)

@admin_bp.route('/deletebrand/<int:id>', methods=["POST"])
def deletebrand(id):
    if 'email' not in session:
        flash('Please Log In first', 'danger')
    
    brand = Brand.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(brand)
        db.session.commit()
        flash(f'Brand: {brand.name} Deleted', 'success')
        return redirect(url_for('admin'))
    flash(f'Brand: {brand.name} cant be Deleted', 'warning')
    return redirect(url_for('admin'))

@admin_bp.route('/deletecategory/<int:id>', methods=["POST"])
def deletecategory(id):
    if 'email' not in session:
        flash('Please Log In first', 'danger')
    
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(category)
        db.session.commit()
        flash(f'Category: {category.name} Deleted', 'success')
        return redirect(url_for('admin'))
    flash(f'Category: {category.name} cant be Deleted', 'warning')
    return redirect(url_for('admin'))

@admin_bp.route('/deleteproduct/<int:id>', methods=["POST"])
def deleteproduct(id):
    if 'email' not in session:
        flash('Please Log In first', 'danger')
    product = Product.query.get_or_404(id)
    if request.method == "POST":
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images/' + product.image_1))
            except Exception as e:
                print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'{product.name} Deleted', 'success')
        return redirect(url_for('admin'))
    flash(f'Cant delete {product.name}', 'warning')
    return redirect(url_for('admin'))
