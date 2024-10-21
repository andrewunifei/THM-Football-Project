import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import TeamsHistoric, Base  # Assuming your TeamsHistoric model is in models.py

def fetch_venue_and_populate(api_key, player): 
    api_url = f'https://v3.football.api-sports.io/players/teams?player={player}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers) # Todos estádios da Inglaterra

    if response.status_code == 200:
        teams_historic_data = response.json()  # Parse JSON response

        # Step 2: Create a database engine
        DATABASE_URL = "postgresql://username:password@localhost:5432/mydatabase"  # Replace with your actual database URL
        engine = create_engine(DATABASE_URL)

        # Create all tables if they don't exist
        Base.metadata.create_all(engine)

        # Step 3: Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Step 4: Insert data into the database
        for record in teams_historic_data:
            new_record = TeamsHistoric(
                player_id=record['player_id'],  # Adjust based on your API response structure
                team_id=record['team_id'],
                seasons=record['seasons']
            )
            session.add(new_record)  # Add new record to the session

        # Step 5: Commit the session
        session.commit()
        print("Data inserted successfully.")

    else:
        print(f"Failed to fetch data from API: {response.status_code}")