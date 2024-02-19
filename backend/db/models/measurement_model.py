from datetime import datetime

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class Measurement(Base):
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    part_number = Column(Integer, index=True)
    value = Column(Float)

    batch_id = Column(Integer, ForeignKey('batch.id'))
    batch = relationship("Batch", back_populates="measurements")

    dim_id = Column(Integer, ForeignKey('dim.id'))
    dim = relationship("Dim", back_populates="measurements")

    __table_args__ = (
        UniqueConstraint('batch_id', 'part_number', 'dim_id', name='measurement_unique_contraint'),
    )
