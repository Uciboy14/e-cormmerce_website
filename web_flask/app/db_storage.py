import sys
sys.path.append('/home/uc-code_tech/my-projects/e-cormmerce_website/web_flask/')
from app import create_app, db

app = create_app('default')

with app.app_context():
	db.create_all()
	session = db.session
