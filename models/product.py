from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.abspath(os.path.dirname(__file__))

print(parent_dir)
sys.path.append(parent_dir)

from cartitem import CartItem
from base_model import BaseModel, Base
from category import Category

class Product(BaseModel, Base):
    __tablename__ = "products"
    name = Column(String(125), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)  
    image_url = Column(String(255))
    category_id = Column(String(125), ForeignKey('categories.id'))
    cart_items = relationship("CartItem", backref="product")

