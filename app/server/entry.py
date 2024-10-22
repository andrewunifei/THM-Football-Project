import os
from dotenv import load_dotenv
from flask import Flask
from routes.venues import venue_routes
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session


if __name__ == '__main__':
    load_dotenv()
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_passwd = os.getenv('POSTGRES_PASSWD')
    DATABASE_URI = f'postgresql://{postgres_user}:{postgres_passwd}@localhost:5432/football-app-db'
    engine = create_engine(DATABASE_URI)
    SessionFactory = sessionmaker(bind=engine)
    Session = scoped_session(SessionFactory)
    app = Flask(__name__)
    venue_routes(app, Session)
    app.run(debug=True)