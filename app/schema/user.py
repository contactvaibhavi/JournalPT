import datetime
from sqlalchemy import Column, DateTime, Integer, String
from services.db import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    user_name = Column(String(255))
    user_email = Column(String(320))
    user_age = Column(Integer)
    user_hash = Column(String(255))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
