#!/bin/usr/python3

from flask import Blueprint, render_template

auth_bp = Blueprint('auth_', __name__)

@auth_bp.route('/login', strict_slashes=False)
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form) 
