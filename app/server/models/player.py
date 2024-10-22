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
    name = Column(String(100), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String(4), nullable=False)
    birth = Column(JSONB, nullable=False)  
    nationality = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    injured = Column(Boolean, nullable=False)
    photo = Column(String(150), nullable=False)
    games_appearances = Column(Integer, nullable=False)  
    games_lineups = Column(Integer, nullable=False)
    minutes_played_total = Column(Integer, nullable=False)
    rating = Column(DECIMAL(2, 1), 
                    CheckConstraint('rating >= 0 AND rating <= 10'), 
                    nullable=False)
    substitutes_in = Column(Integer, nullable=False)
    substitutes_out = Column(Integer, nullable=False)
    bench = Column(Integer, nullable=False)
    shots_on = Column(Integer, nullable=False)
    shots_total = Column(Integer, nullable=False)
    goals_total = Column(Integer, nullable=False)
    goals_conceded = Column(Integer, nullable=False)
    goals_assists = Column(Integer, nullable=False)
    goals_saved = Column(Integer, nullable=False)
    passes_total = Column(Integer, nullable=False)
    passes_key = Column(Integer, nullable=False)
    passes_accuracy = Column(DECIMAL(5, 2), 
                             CheckConstraint('passes_accuracy >= 0 AND passes_accuracy <= 100'), 
                             nullable=False)
    tackles_total = Column(Integer, nullable=False)
    tackles_blocks = Column(Integer, nullable=False)
    tackled_interceptions = Column(Integer, nullable=False)
    duels_total = Column(Integer, nullable=False)
    duels_won_total = Column(Integer, nullable=False)
    dribbles_attempts_total = Column(Integer, nullable=False)
    dribbles_success_total = Column(Integer, nullable=False)
    dribbles_past_total = Column(Integer, nullable=False)
    fouls_drawn_total = Column(Integer, nullable=False)
    fouls_committed_total = Column(Integer, nullable=False)
    cards_yellow_total = Column(Integer, nullable=False)
    cards_red_total = Column(Integer, nullable=False)
    penalty_won_total = Column(Integer, nullable=False)
    penalty_committed_total = Column(Integer, nullable=False)
    penalty_scored_total = Column(Integer, nullable=False)
    penalty_missed_total = Column(Integer, nullable=False)
    penalty_saved_total = Column(Integer, nullable=False)
    team_id = Column(Integer, ForeignKey('team.team_id', ondelete='SET NULL'))

    # Relacionamentos
    team = relationship('Team', foreign_keys=[team_id], back_populates='player')
    teams_historic = relationship('TeamsHistoric', back_populates='player')
    injuries = relationship('Injury', back_populates='player')
    games_statistics = relationship('SGPlayerStatistics', back_populates='player')