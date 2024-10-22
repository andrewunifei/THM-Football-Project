from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from base import Base

# Estádio 
class Venue(Base):
    print(Base)
    __tablename__ = 'venue'

    venue_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    surface = Column(String(25), nullable=False)
    image = Column(String(150), nullable=False)

    # Relacionamentos
    team = relationship('Team', back_populates='venue')
    games = relationship('Game', back_populates='stadium')  