#!/bin/usr/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import sys

sys.path.append("/data/data/com.termux/files/home/e-cormmerce_website/models/")

import base_model
from customer import Customer
from order import Order
from cartitem import CartItem
from product import Product
from category import Category

class DBStorage:
    __engine = None
    __session = None
    
    def __init__(self):
        user = "admin" #os.environ.get('MYSQL_USER')
        pwd = "adminpass" #os.environ.get('MYSQL_PWD')
        host = "localhost" #os.environ.get('MYSQL_HOST', 'localhost')
        db = "ecormmerce_db" #os.environ.get('MYSQL_DB')
        #env = os.environ.get('MYSQL_ENV', 'production') 

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}, pool_pre_ping=True')

        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

        def all(self, cls=None):
            classes = [Customer, Order, Product, CartItem, Category]
            objects = {}

            if cls:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = f'{cls.__name__}.{obj.id}'
                    objects[key] = obj
            elif cls is None:
                for cls in classes:
                    query_result = self.__session.query(cls).all()
                    for obj in query_result:
                        key = f'{cls.__name__}.{obj.id}'
                        objects[key] = obj
            return objects
                

        def new(self, obj):
            self.__session.add(obj)
            
        def save(self):
            self.__session.commit()

        def delete(self, obj=None):
            if obj:
                self.__session.delete(obj)

        def reload(self):
            base_model.Base.metadata.create_all(self.__engine)
            self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

            



                





