import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sub_parent = os.path.dirname(parent_dir)
sys.path.append(sub_parent)

from flask import Blueprint, render_template
from models import storage

product_bp = Blueprint("product", __name__)

@product_bp.route("/products/<id>")
def product(id):
	return render_template('')
