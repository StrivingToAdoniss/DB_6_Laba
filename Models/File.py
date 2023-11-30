from Environment.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


class File(Base):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255), nullable=True)
    uploadDate = Column(DateTime)
    lastEditTime = Column(DateTime)
    format = Column(String(45))
    hasVisualization = Column(Boolean)
    authorId = Column(Integer)
    country = Column(String(45))



