from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .venue import Venue

Base = declarative_base()

# Time
class Team(Base):
    __tablename__ = 'team'

    team_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    code = Column(String(25), nullable=False)
    country = Column(String(50), nullable=False)
    founded = Column(Integer, nullable=False)
    national = Column(Boolean, nullable=False)
    logo = Column(String(150), nullable=False)
    seasons_played = Column(Integer, nullable=False)
    current_season = Column(Integer, nullable=False)
    games_played_home = Column(Integer, nullable=False)
    games_played_away = Column(Integer, nullable=False)
    games_played_total = Column(Integer, nullable=False)
    wins_home = Column(Integer, nullable=False)
    wins_away = Column(Integer, nullable=False)
    wins_total = Column(Integer, nullable=False)
    draws_home = Column(Integer, nullable=False)
    draws_away = Column(Integer, nullable=False)
    draws_total = Column(Integer, nullable=False)
    losses_home = Column(Integer, nullable=False)
    losses_away = Column(Integer, nullable=False)
    losses_total = Column(Integer, nullable=False)
    goals_for_home = Column(Integer, nullable=False)
    goals_for_away = Column(Integer, nullable=False)
    goals_for_total = Column(Integer, nullable=False)
    segments_for = Column(JSONB, nullable=False)  # JSONB no PostgreSQL
    goals_against_home = Column(Integer, nullable=False)
    goals_against_away = Column(Integer, nullable=False)
    goals_against_total = Column(Integer, nullable=False)
    segments_against = Column(JSONB, nullable=False)  # JSONB no PostgreSQL
    biggest_win_home = Column(String(10), nullable=False)
    biggest_win_away = Column(String(10), nullable=False)
    biggest_loss_home = Column(String(10), nullable=False)
    biggest_loss_away = Column(String(10), nullable=False)
    clean_sheet_home = Column(Integer, nullable=False)
    clean_sheet_away = Column(Integer, nullable=False)
    clean_sheet_total = Column(Integer, nullable=False)
    failed_to_score_home = Column(Integer, nullable=False)
    failed_to_score_away = Column(Integer, nullable=False)
    failed_to_score_total = Column(Integer, nullable=False)
    penalty_scored = Column(Integer, nullable=False)
    penalty_missed = Column(Integer, nullable=False)
    yellow_cards = Column(JSONB, nullable=False)
    red_cards = Column(JSONB, nullable=False)
    venue_id = Column(Integer, ForeignKey('venue.venue_id', ondelete='SET NULL'))

    # Relacionamentos
    venue = relationship('Venue', back_populates='team')
    player = relationship('Player', back_populates='team')
    teams_historic = relationship('TeamsHistoric', back_populates='team')