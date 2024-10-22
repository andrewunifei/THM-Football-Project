from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Boolean, CHAR, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base

class SGPlayerStatistics(Base):
    __tablename__ = 'sg_player_statistics'

    player_id = Column(Integer, ForeignKey('player.player_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    player_number = Column(Integer, nullable=True)
    position = Column(CHAR(5), nullable=True)
    rating = Column(DECIMAL(2, 2), 
                   CheckConstraint('rating >= 0 AND rating <= 10'), 
                   nullable=True)
    captain = Column(Boolean, nullable=True)
    substitute = Column(Boolean, nullable=True)
    offsides = Column(Integer, nullable=True)
    shots_on = Column(Integer, nullable=True)
    shots_total = Column(Integer, nullable=True)
    goals_total = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_assists = Column(Integer, nullable=True)
    goals_saves = Column(Integer, nullable=True)
    passes_total = Column(Integer, nullable=True)
    passes_key = Column(Integer, nullable=True)
    passes_accuracy = Column(DECIMAL(5, 2), 
                             CheckConstraint('passes_accuracy >= 0 AND passes_accuracy <= 100'), 
                             nullable=True)
    tackles_total = Column(Integer, nullable=True)
    blocks = Column(Integer, nullable=True)
    interceptions = Column(Integer, nullable=True)
    duels_total = Column(Integer, nullable=True)
    duels_won = Column(Integer, nullable=True)
    dribbles_attempts = Column(Integer, nullable=True)
    dribbles_success = Column(Integer, nullable=True)
    dribbles_past = Column(Integer, nullable=True)
    fouls_drawn = Column(Integer, nullable=True)
    fouls_committed = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    penalty_won = Column(Integer, nullable=True)
    penalty_committed = Column(Integer, nullable=True)
    penalty_scored = Column(Integer, nullable=True)
    penalty_missed = Column(Integer, nullable=True)
    penalty_saved = Column(Integer, nullable=True)

    # Relationships
    player = relationship('Player', foreign_keys=[player_id], back_populates='games_statistics')  # Assuming Player class exists
    game = relationship('Game', foreign_keys=[game_id], back_populates='players_statistics')      # Assuming Game class exists