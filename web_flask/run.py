from app import create_app, db
#from app.models import Customer, Product, Category, Order, Cart
from flask_migrate import Migrate


app = create_app('default')
migrate = Migrate(app, db)

if __name__ == '__main__':
	app.run(debug=True, port=8080)
