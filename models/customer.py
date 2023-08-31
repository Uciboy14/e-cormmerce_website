#!/bin/usr/python3
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(working_path)

from base_model import BaseModel, Base
#from cartitem import CartItem
#from order import Order
#from category import Category
#from product import Product
#from base_model import BaseModel, Base

class Customer(BaseModel, Base):
    __tablename__ = "customers"
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    cart_items = relationship('CartItem', backref='customer')
    orders = relationship('Order', backref='customer')
