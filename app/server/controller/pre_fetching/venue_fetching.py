import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.venue import Venue, Base


def fetch_venue(postgres_user, postgres_passwd, api_key):
    country = 'England'
    premier_league = 39
    season = 2022
    api_url = f'https://v3.football.api-sports.io/venues?country={country}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers) # All stadium from england

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
            for key, value in venue.items(): 
                if venue[key] is None: 
                        venue[key] = 0

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