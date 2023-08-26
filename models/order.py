from base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

class Order(BaseModel, Base):
    __tablename__ = 'orders'
    user_id = Column(Integer, ForeignKey('customer.id'))
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default='Pending')

