from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SGTeamStatistics(Base):
    __tablename__ = 'sg_team_statistics'

    game_id = Column(Integer, ForeignKey('game.game_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    team_id = Column(Integer, ForeignKey('team.team_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    shots_on_goal = Column(Integer, nullable=False)
    shots_off_goal = Column(Integer, nullable=False)
    total_shots = Column(Integer, nullable=False)
    blocked_shots = Column(Integer, nullable=False)
    shots_insidebox = Column(Integer, nullable=False)
    shots_outsidebox = Column(Integer, nullable=False)
    fouls = Column(Integer, nullable=False)
    corner_kicks = Column(Integer, nullable=False)
    offsides = Column(Integer, nullable=False)
    yellow_cards = Column(Integer, nullable=False)
    red_cards = Column(Integer, nullable=False)
    goalkeeper_saves = Column(Integer, nullable=False)
    total_passes = Column(Integer, nullable=False)
    passes_accurate = Column(Integer, nullable=False)

    # Ball possession and passes percentage with constraints
    ball_possession = Column(DECIMAL(5, 2), 
                             CheckConstraint('ball_possession >= 0 AND ball_possession <= 100'), 
                             nullable=False)
    passes_percentage = Column(DECIMAL(5, 2), 
                               CheckConstraint('passes_percentage >= 0 AND passes_percentage <= 100'), 
                               nullable=False)
    expected_goals = Column(DECIMAL(5, 2), 
                            CheckConstraint('expected_goals >= 0 AND expected_goals <= 100'), 
                            nullable=False)

    # Relationships
    game = relationship("Game", back_populates="teams_statistics")  # Assuming Game class exists
    team = relationship("Team", back_populates="team_statistics")   # Assuming Team class exists