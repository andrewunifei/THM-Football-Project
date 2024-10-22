from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Injury(Base):
    __tablename__ = 'injuries'

    player_id = Column(Integer, ForeignKey('player.player_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    type = Column(String(50), nullable=False)
    reason = Column(String(100), nullable=False)

    # Check Constraint for type
    __table_args__ = (
        CheckConstraint(type.in_(['Missing Fixture', 'Questionable']), name='check_injury_type'),
    )

    # Relationships
    player = relationship("Player", back_populates="injuries")  # Assuming Player class exists
    game = relationship("Game", back_populates="injuries")      # Assuming Game class exists