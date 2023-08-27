
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append(working_path)

from models.base_model import BaseModel, Base

class Order(BaseModel, Base):
    __tablename__ = 'orders'
    customer_id = Column(String(125), ForeignKey('customers.id'))
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default='Pending')
    customer = relationship("Customer", back_populates="orders")

