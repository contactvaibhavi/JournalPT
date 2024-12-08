import datetime
from sqlalchemy import JSON, Column, ForeignKey, Integer, String, DateTime
from services.db import Base


class LlmCall(Base):
    __tablename__ = 'llm_calls'
    llm_call_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    user_id = Column(ForeignKey('users.user_id'), nullable=True)
    model = Column(String)
    type = Column(String)

    input_tokens = Column(Integer)
    output_tokens = Column(Integer)
    meta = Column(JSON, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}