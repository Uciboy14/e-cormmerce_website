
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(working_path)


from category import Category
from product import Product
from base_model import BaseModel, Base
from cartitem import CartItem

class Order(BaseModel, Base):
    __tablename__ = 'orders'
    customer_id = Column(String(125), ForeignKey('customers.id'))
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default='Pending')
    

