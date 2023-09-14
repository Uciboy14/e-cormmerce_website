from flask import Flask, Blueprint, render_template

customer_bp = Blueprint('customer', __name__, 
                       template_folder='templates',
                       static_folder='static')

@customer_bp.route('/customer')
def customer():
    return render_template('')
