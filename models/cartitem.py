from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append("/data/data/com.termux/files/home/e-cormmerce_website/")

from models.base_model import BaseModel, Base

class CartItem(BaseModel, Base):
    __tablename__ = 'cart_items'
    # ... updated column
    customer_id = Column(String(125), ForeignKey('customers.id'))
    product_id = Column(String(125), ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    customer = relationship("Customer", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
