from Environment.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Request(Base):
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    target = Column(String(255))
    type = Column(String(45))
    date = Column(DateTime)
    user_id = Column(Integer)



