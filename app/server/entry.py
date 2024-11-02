import os
from dotenv import load_dotenv
from flask import Flask
from routes.venue_routes import venue_routes
from routes.team_routes import team_routes
from routes.game_routes import game_routes
from routes.player_routes import player_routes
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
import threading
from poll_fetching import run_schedule
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    load_dotenv()
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_passwd = os.getenv('POSTGRES_PASSWD')

    DATABASE_URI = f'postgresql://{postgres_user}:{postgres_passwd}@localhost:5432/football-app-db'
    engine = create_engine(DATABASE_URI)
    SessionFactory = sessionmaker(bind=engine)
    Session = scoped_session(SessionFactory)
    api_key = os.getenv('API_KEY')
    league = 39
    season = 2022

    scheduler_thread = threading.Thread(target=run_schedule, args=(league, season, Session, api_key, engine), daemon=True)
    scheduler_thread.start()
    
    app = Flask(__name__)
    venue_routes(app, Session)
    team_routes(app, Session)
    game_routes(app, Session)
    player_routes(app, Session)
    app.run(debug=True)

