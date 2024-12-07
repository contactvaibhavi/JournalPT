from sqlalchemy import Column, Integer, String
from services.db_service import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(255))
    user_email = Column(String(320))
    user_age = Column(Integer)
    user_hash = Column(String(255))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
