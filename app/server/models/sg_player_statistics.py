from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Boolean, CHAR, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SGPlayerStatistics(Base):
    __tablename__ = 'sg_player_statistics'

    player_id = Column(Integer, ForeignKey('player.player_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    player_number = Column(Integer, nullable=False)
    position = Column(CHAR(5), nullable=False)
    rating = Column(DECIMAL(2, 2), 
                   CheckConstraint('rating >= 0 AND rating <= 10'), 
                   nullable=False)
    captain = Column(Boolean, nullable=False)
    substitute = Column(Boolean, nullable=False)
    offsides = Column(Integer, nullable=False)
    shots_on = Column(Integer, nullable=False)
    shots_total = Column(Integer, nullable=False)
    goals_total = Column(Integer, nullable=False)
    goals_conceded = Column(Integer, nullable=False)
    goals_assists = Column(Integer, nullable=False)
    goals_saves = Column(Integer, nullable=False)
    passes_total = Column(Integer, nullable=False)
    passes_key = Column(Integer, nullable=False)
    passes_accuracy = Column(DECIMAL(5, 2), 
                             CheckConstraint('passes_accuracy >= 0 AND passes_accuracy <= 100'), 
                             nullable=False)
    tackles_total = Column(Integer, nullable=False)
    blocks = Column(Integer, nullable=False)
    interceptions = Column(Integer, nullable=False)
    duels_total = Column(Integer, nullable=False)
    duels_won = Column(Integer, nullable=False)
    dribbles_attempts = Column(Integer, nullable=False)
    dribbles_success = Column(Integer, nullable=False)
    dribbles_past = Column(Integer, nullable=False)
    fouls_drawn = Column(Integer, nullable=False)
    fouls_committed = Column(Integer, nullable=False)
    yellow_cards = Column(Integer, nullable=False)
    red_cards = Column(Integer, nullable=False)
    penalty_won = Column(Integer, nullable=False)
    penalty_committed = Column(Integer, nullable=False)
    penalty_scored = Column(Integer, nullable=False)
    penalty_missed = Column(Integer, nullable=False)
    penalty_saved = Column(Integer, nullable=False)

    # Relationships
    player = relationship("Player", back_populates="games_statistics")  # Assuming Player class exists
    game = relationship("Game", back_populates="players_statistics")      # Assuming Game class exists