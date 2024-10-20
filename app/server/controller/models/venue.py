from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Estádio 
class Venue(Base):
    __tablename__ = 'venue'

    venue_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    surface = Column(String(25), nullable=False)
    image = Column(String(150), nullable=False)