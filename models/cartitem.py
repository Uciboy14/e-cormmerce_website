from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from base_model import BaseModel, Base
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append(parent_dir)

from models.base_model import BaseModel, Base

class CartItem(BaseModel, Base):
    __tablename__ = 'cart_items'
    customer_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
