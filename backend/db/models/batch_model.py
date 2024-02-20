from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Batch(Base):
    __tablename__ = 'batch'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    measurements = relationship("Measurement", back_populates="batch")
