from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append('/home/uc-code_tech/my-projects/e-cormmerce_website/')

import models
from models.base_model import BaseModel, Base

class Product(BaseModel, Base):
    __tablename__ = "products"
    name = Column(String(125), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)  
    image_url = Column(String(255))
    category_id = Column(String(125), ForeignKey('categories.id'))

    cart_items = relationship("CartItem", back_populates="product")
    category = relationship("Category", back_populates="products")

