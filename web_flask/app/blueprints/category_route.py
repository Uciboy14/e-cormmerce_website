import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sub_parent = os.path.dirname(parent_dir)
sys.path.append(sub_parent)

from flask import Blueprint, render_template
from models import storage

category_bp = Blueprint("category", __name__)

@category_bp.route('/categories', defaults={'id': None})
@category_bp.route('/categories/<id>')
def categories(id):
	return render_template('category.html')