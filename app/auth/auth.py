import sys

sys.path.append('/data/data/com.termux/files/home/storage/shared/anoda/')

from flask import Flask, Blueprint, render_template, session, request, redirect, url_for, flash
from app import app, db
from app.auth.forms.register import RegistrationForm
from app.auth.forms.login import LoginForm
#from app.admin.models import User
#from app.products.models.product import Product
#from app.products.models.brand import Brand
#from app.products.models.category import Category

auth_bp = Blueprint('auth', __name__, 
                    template_folder='templates',
                    static_folder='static')


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=hash_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {form.name.data},Thank You for registering", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Register")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session["email"] = form.email.data
            flash(f"Welcome, {user.username}. You are now logged in.", "success")
            return redirect(url_for("admin.login"))

    return render_template("login.html", form=form, title="Log In")    