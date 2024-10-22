from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base

class Injury(Base):
    __tablename__ = 'injury'

    player_id = Column(Integer, ForeignKey('player.player_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    type = Column(String(50), nullable=True)
    reason = Column(String(100), nullable=True)

    # Check Constraint for type
    __table_args__ = (
        CheckConstraint(type.in_(['Missing Fixture', 'Questionable']), name='check_injury_type'),
    )

    # Relationships
    player = relationship('Player', back_populates='injuries')  # Assuming Player class exists
    game = relationship('Game', back_populates='injuries')      # Assuming Game class exists