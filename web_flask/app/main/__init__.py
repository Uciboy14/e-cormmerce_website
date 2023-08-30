#!/bin/usr/python3 

from flask import Blueprint
import os
import sys

sys.path.append('/home/uc-code_tech/my-projects/e-cormmerce_website/web_flask/app/')
route_bp = Blueprint('route', __name__)

from main import routes, errors
