#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append("/data/data/com.termux/files/home/e-cormmerce_website/")

#import models
from models.base_model import BaseModel, Base
#from models.customer import Customer
#from models.order import Order
#from models.product import Product
#from models.category import Category
#from models.cartitem import CartItem
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#classes = {"Customer": Customer, "Product": Product,
           #"Order": Order, "Category": Category, "CartItem": CartItem}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        #HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        #HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        #HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        #HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqlconnector://hbnb_dev:four1cup@127.0.0.1/hbnb_dev_db", pool_pre_ping=True)
        #self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      #format(HBNB_MYSQL_USER,
                                             #HBNB_MYSQL_PWD,
                                             #HBNB_MYSQL_HOST,
                                             #HBNB_MYSQL_DB))
        #if HBNB_ENV == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        from models.customer import Customer
        from models.order import Order
        from models.product import Product
        from models.category import Category
        from models.cartitem import CartItem

        classes = {"Customer": Customer, "Product": Product, "Order": Order, "Category": Category, "CartItem": CartItem}

        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls=None, id=None):
        """Returns obj based on class name and its ID"""
        if cls is not None and id is not None:
            try:
                return self.__session.query(classes[cls]).get(id)
            except:
                return None

        return None

    def count(self, cls=None):
        """Returns the amount of objects"""
        if cls is not None:
            try:
                return len(self.all(classes[cls]))
            except:
                return None
        else:
            return len(self.all())
