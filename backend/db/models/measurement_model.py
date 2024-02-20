from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Measurement(Base):
    __tablename__ = 'measurement'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    part_number = Column(Integer)
    value = Column(Float)

    batch_id = Column(Integer, ForeignKey('batch.id'))
    batch = relationship("Batch", back_populates="measurements")

    # Ensure dim_id remains unique as per your initial model.
    dim_id = Column(Integer, ForeignKey('dim.id'), unique=True)
    dim = relationship("Dim", back_populates="measurements")
