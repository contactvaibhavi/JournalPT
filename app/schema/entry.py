import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from services.db import Base


class Entry(Base):
    __tablename__ = 'entrys'
    entry_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    user_id = Column(Integer, ForeignKey('users.user_id'))
    content = Column(String)
    date = Column(Date)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}