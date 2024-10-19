import sys
import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

sys.path.insert(1, os.path.abspath('../../models/venue.py'))

import Venue, Base

load_dotenv()

postgres_user = os.getenv('POSTGRES_USER')
postgres_passwd = os.getenv('POSTGRES_PASSWD')
api_key = os.getenv('API_KEY')
country = 'England'
premier_league = 39
season = 2022
api_url = f'https://v3.football.api-sports.io/venues?country={country}'
headers = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': api_key
}
response = requests.get(url, headers=headers) # All stadium from england

if response.status_code == 200:
    venues_data = response.json()
    number_of_results = venues_data['results']
    DATABASE_URL = f'postgresql://{postgres_user}:{postgres_passwd}@localhost:5432/football-app-db'
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    print(f'Adicionando {number_of_results} novas instâncias da tabela Venue')

    # Insert data into the database
    for venue in venues_data['response']:
        new_venue = Venue(
            venue_id=venue['id'],
            name=venue['name'],
            address=venue['address'],
            city=venue['city'],
            country=venue['country'],
            capacity=venue['capacity'],
            surface=venue['surface'],
            image=venue['image']
        )
        session.add(new_venue)

    session.commit()
    print("Data inserted successfully.")

else:
    print(f"Failed to fetch data from API: {response.status_code}")