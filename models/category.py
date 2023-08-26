#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class Category(BaseModel, Base):
    __tablename__ = 'categories'
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category')

