from sqlalchemy import create_engine, Table, update

def get_teams_ids():
    url = 'http://127.0.0.1:5000/teams-id'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []

def fetch_standing_and_populate(league, season, api_key, db_session, metadata, engine):
    teams_ids = get_teams_ids()
    if(len(teams_ids) == 0):
        return

    team_table = Table('team', metadata, autoload_with=engine)
    stmt = ()
    
    for team_id in teams_ids:
        standing_endpoint = f'standings?league={league}&season={season}&team={team_id}'
        api_url = f'https://v3.football.api-sports.io/{standing_endpoint}'
        headers = {
            'x-rapidapi-host': 'v3.football.api-sports.io',
            'x-rapidapi-key': api_key
        }
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            data = data['response']
            data_to_insert = {
                'rank': data['league']['standings']['rank'],
                'points': data['league']['standings']['points']
            }
            
            stmt = (
                update(team_table)
                .where(teams_ids.c.team_id == team_id)  
                .values(**data_to_insert)
            )

            with engine.connect() as conn:
                conn.execute(stmt)

        print('Data inserted successfully.')

    else:
        print(f'Failed to fetch data from API: {response.status_code}')