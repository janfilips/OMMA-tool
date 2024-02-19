from datetime import datetime

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

class Dim(Base):
    __tablename__ = 'dim'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    tol_nominal = Column(Float, nullable=True)
    tol_upper = Column(Float, nullable=True)
    tol_lower = Column(Float, nullable=True)

    measurements = relationship("Measurement", back_populates="dim")
