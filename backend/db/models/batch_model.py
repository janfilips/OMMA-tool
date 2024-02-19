from datetime import datetime

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

class Batch(Base):
    __tablename__ = 'batch'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    measurements = relationship("Measurement", back_populates="batch")
