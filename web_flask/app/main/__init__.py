#!/bin/usr/python3 

from flask import Blueprint
import os
import sys

working_path = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(working_path)
sys.path.append(parent_dir)

route_bp = Blueprint('route', __name__)

from main import routes, errors
