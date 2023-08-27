#!/bin/usr/python3
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append(working_path)

from models.base_model import BaseModel, Base

class Category(BaseModel, Base):
    __tablename__ = 'categories'
    name = Column(String(50), nullable=False)
    products = relationship('Product', back_populates='category')

