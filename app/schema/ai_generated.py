import datetime
from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String, DateTime
from pgvector.sqlalchemy import Vector
from  api.v1 import llm
from services.db import Base


class AiGenerated(Base):
    __tablename__ = 'ai_generateds'
    aigenerated_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    user_id = Column(ForeignKey('users.user_id'))
    llm_call_id = Column(ForeignKey('llm_calls.llm_call_id'), nullable=True)
    type = Column(String)

    entry_ids = Column(ARRAY(Integer), default=[])
    aigenerated_ids = Column(ARRAY(Integer), default=[])
    
    content = Column(String, nullable=True)
    embeddings = Column(Vector, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}