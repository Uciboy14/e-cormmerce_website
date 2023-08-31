from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(working_path)

from base_model import BaseModel, Base

class CartItem(BaseModel, Base):
    __tablename__ = 'cart_items'
    # ... updated column
    customer_id = Column(String(125), ForeignKey('customers.id'))
    product_id = Column(String(125), ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
