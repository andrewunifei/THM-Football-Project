import requests
from .models.team import Team
from .models.game import Game
from .models.venue import Venue

# Esses dados são referentes a entidade 'Estádio' no diagrama ER
def fetch_venue_and_populate(
        api_key,
        country,
        db_session
    ):
    api_url = f'https://v3.football.api-sports.io/venues?country={country}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers) # Todos estádios da Inglaterra

    if response.status_code == 200:
        venues_data = response.json()
        number_of_results = venues_data['results']
        print(f'Adicionando {number_of_results} novas instâncias da tabela Venue')

        # Inserindo dados no banco de dados
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
            db_session.add(new_venue)

        db_session.commit()
        print('Dados inseridos com sucesso.')

    else:
        print(f'Comunicação com a API falhou com código: {response.status_code}')