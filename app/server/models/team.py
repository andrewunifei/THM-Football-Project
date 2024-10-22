from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from base import Base

# Time
class Team(Base):
    print(Base)
    __tablename__ = 'team'

    team_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    code = Column(String(25), nullable=False)
    country = Column(String(50), nullable=False)
    founded = Column(Integer, nullable=False)
    national = Column(Boolean, nullable=False)
    logo = Column(String(150), nullable=False)
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
    venue = relationship('Venue', foreign_keys=[venue_id], back_populates='team')
    player = relationship('Player', back_populates='team')
    teams_historic = relationship('TeamsHistoric', back_populates='team')
    home_games = relationship('Game', foreign_keys='Game.home_team_id', back_populates='home_team') 
    away_games = relationship('Game', foreign_keys='Game.away_team_id', back_populates='away_team') 
    games_won = relationship('Game', foreign_keys='Game.winner_team_id', back_populates='winner_team') 
    team_statistics = relationship('SGTeamStatistics', back_populates='team')