import os
import sys

sys.path.append('/data/data/com.termux/files/home/storage/shared/anoda/')

from app import app, db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}  # Add this line
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

with app.app_context():
  db.create_all()
  db.session.commit()

