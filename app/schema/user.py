from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(255))
    user_age = Column(Integer)
