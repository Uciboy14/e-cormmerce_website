#!/bin/usr/python3
from base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class Customer:
    __tablename__ = "customers"
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    cart_items = relationship('CartItem', backref='user')
    orders = relationship('Order', backref='user')
