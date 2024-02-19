from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Batch(Base):
    __tablename__ = 'batch'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    measurements = relationship("Measurement", back_populates="batch")
