from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DECIMAL,
    CheckConstraint
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base

# Jogador
class Player(Base):
    __tablename__ = 'player'

    player_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String(4), nullable=True)
    birth = Column(JSONB, nullable=True)  
    nationality = Column(String(50), nullable=True)
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    injured = Column(Boolean, nullable=True)
    photo = Column(String(150), nullable=True)
    games_appearences = Column(Integer, nullable=True)  
    games_lineups = Column(Integer, nullable=True)
    minutes_played_total = Column(Integer, nullable=True)
    rating = Column(DECIMAL(2, 1), 
                    CheckConstraint('rating >= 0 AND rating <= 10'), 
                    nullable=True)
    substitutes_in = Column(Integer, nullable=True)
    substitutes_out = Column(Integer, nullable=True)
    bench = Column(Integer, nullable=True)
    shots_on = Column(Integer, nullable=True)
    shots_total = Column(Integer, nullable=True)
    goals_total = Column(Integer, nullable=True)
    goals_conceded = Column(Integer, nullable=True)
    goals_assists = Column(Integer, nullable=True)
    goals_saved = Column(Integer, nullable=True)
    passes_total = Column(Integer, nullable=True)
    passes_key = Column(Integer, nullable=True)
    passes_accuracy = Column(DECIMAL(5, 2), 
                             CheckConstraint('passes_accuracy >= 0 AND passes_accuracy <= 100'), 
                             nullable=True)
    tackles_total = Column(Integer, nullable=True)
    tackles_blocks = Column(Integer, nullable=True)
    tackled_interceptions = Column(Integer, nullable=True)
    duels_total = Column(Integer, nullable=True)
    duels_won_total = Column(Integer, nullable=True)
    dribbles_attempts_total = Column(Integer, nullable=True)
    dribbles_success_total = Column(Integer, nullable=True)
    dribbles_past_total = Column(Integer, nullable=True)
    fouls_drawn_total = Column(Integer, nullable=True)
    fouls_committed_total = Column(Integer, nullable=True)
    cards_yellow_total = Column(Integer, nullable=True)
    cards_red_total = Column(Integer, nullable=True)
    penalty_won_total = Column(Integer, nullable=True)
    penalty_committed_total = Column(Integer, nullable=True)
    penalty_scored_total = Column(Integer, nullable=True)
    penalty_missed_total = Column(Integer, nullable=True)
    penalty_saved_total = Column(Integer, nullable=True)
    team_id = Column(Integer, ForeignKey('team.team_id', ondelete='SET NULL'))

    # Relacionamentos
    team = relationship('Team', foreign_keys=[team_id], back_populates='player')
    teams_historic = relationship('TeamsHistoric', back_populates='player')
    injuries = relationship('Injury', back_populates='player')
    games_statistics = relationship('SGPlayerStatistics', back_populates='player')