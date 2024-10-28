from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, CheckConstraint, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import Base

class SGTeamStatistics(Base):
    __tablename__ = 'sg_team_statistics'

    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    team_id = Column(Integer, ForeignKey('team.team_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    shots_on_goal = Column(Integer, nullable=True)
    shots_off_goal = Column(Integer, nullable=True)
    total_shots = Column(Integer, nullable=True)
    blocked_shots = Column(Integer, nullable=True)
    shots_insidebox = Column(Integer, nullable=True)
    shots_outsidebox = Column(Integer, nullable=True)
    fouls = Column(Integer, nullable=True)
    corner_kicks = Column(Integer, nullable=True)
    offsides = Column(Integer, nullable=True)
    yellow_cards = Column(Integer, nullable=True)
    red_cards = Column(Integer, nullable=True)
    goalkeeper_saves = Column(Integer, nullable=True)
    total_passes = Column(Integer, nullable=True)
    passes_accurate = Column(Integer, nullable=True)
    ball_possession = Column(String(50), nullable=True)
    passes_percentage = Column(String(50), nullable=True)

    # Relationships
    game = relationship('Game', back_populates='teams_statistics')  # Assuming Game class exists
    team = relationship('Team', back_populates='team_statistics')   # Assuming Team class exists