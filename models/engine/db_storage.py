import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
project_dir = os.path.dirname(parent_dir)
sys.path.append(project_dir)

from models.customer import Customer
from models.product import Product
from models.order import Order
from models.cartitem import CartItem
from models.category import Category
#from models.amenity import Amenity

class DBStorage:
    """ Responsible for storing information into tthe database and retrieving it"""
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """ Calling the Construstor method"""
        pwd = "adminpass" #os.getenv('HBNB_MYSQL_PWD')
        user = "admin" #os.getenv('HBNB_MYSQL_USER')
        #env = "test" #os.getenv('HBNB_ENV')
        db = "ecormmerce_db" #os.getenv('HBNB_MYSQL_DB')
        host = "localhost" #os.getenv('HBNB_MYSQL_HOST')

        self.classes = [User, State, City, Place, Review]

        self.__engine = create_engine(f"mysql+mysqlconnector://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)

        if env == "dev":
            # Drop all tables from database
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries on the database all objects on the tables information"""
        if cls is None:
            for cls in self.classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    self.__objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                self.__objects[key] = obj
        return self.__objects

    def new(self, obj=None):
        """ Add new records to the table in the datbase"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ Commit all your changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes object from the database """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload method"""
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create the current database session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ call remove() method on the private session attribute """
        self.__session.close()

    def delete_db(self):
        self.__engine(f"DROP DATABASE {self.db};")

