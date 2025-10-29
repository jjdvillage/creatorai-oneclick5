from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    plan = Column(String, default='free')
    created_at = Column(DateTime, default=datetime.utcnow)

class Usage(Base):
    __tablename__ = 'usage'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    year = Column(Integer, index=True)
    month = Column(Integer, index=True)
    generations = Column(Integer, default=0)
