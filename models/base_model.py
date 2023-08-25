#
#/bin/usr/python3
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

time_format = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

class BaseModel:
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            if key == '__class__':
                pass


    def __str__(self):
        pass

    def to_dict(self):
        pass
        
    def save(self):
        models.storage.new()
    
    def delete(self):
        pass

    
        
