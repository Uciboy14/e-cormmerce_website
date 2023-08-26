from base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship

class Product(BaseModel, Base):
    __tablename__ = "products"
    name = Column(String(125), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)  
    image_url = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    cart_items = relationship('CartItem', backref='product')

