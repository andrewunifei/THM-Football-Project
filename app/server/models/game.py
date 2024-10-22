from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from base import Base

class Game(Base):
    __tablename__ = 'game'

    game_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    referee = Column(String(50), nullable=True)
    timezone = Column(String(10), nullable=True)
    date = Column(TIMESTAMP(6), nullable=True)
    first_period = Column(TIMESTAMP(6), nullable=True)
    second_period = Column(TIMESTAMP(6), nullable=True)
    score = Column(JSONB, nullable=True)  # JSON object
    home_team_goals = Column(Integer, nullable=True)
    away_team_goals = Column(Integer, nullable=True)

    # Relações Estrangeiras refletidas na Camada Banco de Dados
    venue_id = Column(Integer, ForeignKey('venue.venue_id', ondelete='SET NULL'), nullable=False)
    home_team_id = Column(Integer, ForeignKey('team.team_id', ondelete='SET NULL'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('team.team_id', ondelete='SET NULL'), nullable=False)
    winner_team_id = Column(Integer, ForeignKey('team.team_id', ondelete='SET NULL'), nullable=False)

    # Relações para acessar na Camada ORM 
    stadium = relationship('Venue', back_populates='games')  
    home_team = relationship('Team', foreign_keys=[home_team_id], back_populates='home_games') 
    away_team = relationship('Team', foreign_keys=[away_team_id], back_populates='away_games') 
    winner_team = relationship('Team', foreign_keys=[winner_team_id], back_populates='games_won') 
    injuries = relationship('Injury', back_populates='game')
    teams_statistics = relationship('SGTeamStatistics', back_populates='game')
    players_statistics = relationship('SGPlayerStatistics', back_populates='game')      # Assuming Game class exists