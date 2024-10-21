from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Hitórico de Times do Jogador
class TeamsHistoric(Base):
    __tablename__ = 'teams_historic'

    player_id = Column(Integer, ForeignKey('player.player_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    team_id = Column(Integer, ForeignKey('team.team_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    seasons = Column(Integer, nullable=False)

    # Relacionamentos
    player = relationship('Player', back_populates='teams_historic')
    team = relationship('Team', back_populates='teams_historic')