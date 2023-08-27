
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append("/data/data/com.termux/files/home/e-cormmerce_website/")

from models.cartitem import CartItem
from models.category import Category
from models.product import Product
from models.base_model import BaseModel, Base

class Order(BaseModel, Base):
    __tablename__ = 'orders'
    customer_id = Column(String(125), ForeignKey('customers.id'))
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default='Pending')
    customer = relationship("Customer", back_populates="orders")

