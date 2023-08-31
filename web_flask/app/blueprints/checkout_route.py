import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sub_parent = os.path.dirname(parent_dir)
sys.path.append(sub_parent)

from flask import Blueprint, render_template
from models import storage

checkout_bp = Blueprint("checkout", __name__)

@checkout_bp.route("/checkout")
def checkout():
	return render_template('checkout.html')
