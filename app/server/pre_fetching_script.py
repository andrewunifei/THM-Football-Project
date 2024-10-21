import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from controller.pre_fetching.venue_fetching import fetch_venue_and_populate
from controller.pre_fetching.team_fetching import fetch_team_and_populate
from controller.pre_fetching.player_fetching import fetch_player_and_populate
from dotenv import load_dotenv

load_dotenv()

postgres_user = os.getenv('POSTGRES_USER')
postgres_passwd = os.getenv('POSTGRES_PASSWD')
api_key = os.getenv('API_KEY')
DATABASE_URL = f'postgresql://{postgres_user}:{postgres_passwd}@localhost:5432/football-app-db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()
inspector = inspect(engine)

table_names = inspector.get_table_names()
print("Existing tables:", table_names)

country = 'England'
league = 39 # Premier League
season = 2022

# fetch_venue_and_populate(api_key, country, db_session)
fetch_team_and_populate(api_key, league, season, db_session)

db_session.close()