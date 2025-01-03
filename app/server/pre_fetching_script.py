import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.ext.declarative import declarative_base
from pre_fetching.venue_fetching import fetch_venue_and_populate
from pre_fetching.team_fetching import fetch_team_and_populate
from pre_fetching.player_fetching import fetch_player_and_populate
from pre_fetching.game_fetching import fetch_game_and_populate
from pre_fetching.injury_fetching import fetch_injury_and_populate
from pre_fetching.sg_team_fetching import fetch_sg_team_and_populate
from pre_fetching.sg_player_fetching import fetch_sg_player_and_populate
from dotenv import load_dotenv

load_dotenv()

postgres_user = os.getenv('POSTGRES_USER')
postgres_passwd = os.getenv('POSTGRES_PASSWD')
api_key = os.getenv('API_KEY')
DATABASE_URL = f'postgresql://{postgres_user}:{postgres_passwd}@localhost:5432/football-app-db'
engine = create_engine(DATABASE_URL)
metadata = MetaData()
Session = sessionmaker(bind=engine)
db_session = Session()

country = 'England'
league = 39 # Premier League
season = 2022

# -- Inseridos com sucesso --
# fetch_venue_and_populate(api_key, country, db_session)
# fetch_team_and_populate(api_key, league, season, db_session)
# fetch_player_and_populate(api_key, league, season, db_session)
# fetch_game_and_populate(api_key, league, season, db_session)
# fetch_injury_and_populate(api_key, league, season, db_session)

# -- Precisam ser inseridos --
# fetch_sg_team_and_populate(api_key, db_session)
# fetch_sg_player_and_populate(api_key, db_session)
# fetch_standing_and_populate(api_key, db_session)

db_session.close()