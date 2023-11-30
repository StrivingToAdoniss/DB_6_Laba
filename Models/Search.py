from Environment.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Search(Base):
    __tablename__ = 'search'
    request_id = Column(Integer, nullable=False)
    file_id = Column(Integer, nullable=False)




