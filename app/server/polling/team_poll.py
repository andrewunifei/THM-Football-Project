import requests
from models.team import Team

def handle_polling_team(db_session, team_id):
    all_columns = Team.__table__.column.keys()
    excluded_columns = {
        'team_id',
        'name',
        'code',
        'country',
        'founded',
        'national', 
        'logo',
        'venue_id', 
        'rank',
        'id'
    }
    selected_columns = [col for col in all_columns if col not in excluded_columns]

    team_information_endpoint = f'teams?league={league}&season={season}'
    api_url = f'https://v3.football.api-sports.io/{team_information_endpoint}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        teams_data = response.json()
        for team_data in teams_data['response']:
            for key, value in team_data.items(): 
                if team_data[key] is None: 
                        team_data[key] = 0

            team_statistics = {}
            team_id = team_data['team']['id']
            team_statistics_endpoint = f'teams/statistics?league={league}&season={season}&team={team_id}'
            api_url = f'https://v3.football.api-sports.io/{team_statistics_endpoint}'
            response = requests.get(api_url, headers=headers)

            if response.status_code == 200:
                team_statistics = response.json()
                team_statistics = team_statistics['response']

                # O time já existe no banco de dados
                # Essa lógica é para atualizar apenas as novas informações depois de um novo jogo
                selected_team = db_session.query(Team).filter(Team.team_id == team_id).first()
                if selected_team:
                    setattr(selected_team, selected_columns[0], team_statistics['fixtures']['played']['home'])
                    setattr(selected_team, selected_columns[1], team_statistics['fixtures']['played']['away'])
                    setattr(selected_team, selected_columns[2], team_statistics['fixtures']['played']['total'])
                    setattr(selected_team, selected_columns[3], team_statistics['fixtures']['wins']['home'])
                    setattr(selected_team, selected_columns[4], team_statistics['fixtures']['wins']['away'])
                    setattr(selected_team, selected_columns[5], team_statistics['fixtures']['wins']['total'])
                    setattr(selected_team, selected_columns[6], team_statistics['fixtures']['draws']['home'])
                    setattr(selected_team, selected_columns[7], team_statistics['fixtures']['draws']['away'])
                    setattr(selected_team, selected_columns[8], team_statistics['fixtures']['draws']['total'])
                    setattr(selected_team, selected_columns[9], team_statistics['fixtures']['loses']['home'])
                    setattr(selected_team, selected_columns[10], team_statistics['fixtures']['loses']['away'])
                    setattr(selected_team, selected_columns[11], team_statistics['fixtures']['loses']['total'])
                    setattr(selected_team, selected_columns[12], team_statistics['goals']['for']['total']['home'])
                    setattr(selected_team, selected_columns[13], team_statistics['goals']['for']['total']['away'])
                    setattr(selected_team, selected_columns[14], team_statistics['goals']['for']['total']['total'])
                    setattr(selected_team, selected_columns[15], team_statistics['goals']['for']['minute']), # JSON objec)
                    setattr(selected_team, selected_columns[16], team_statistics['goals']['against']['total']['home'])
                    setattr(selected_team, selected_columns[17], team_statistics['goals']['against']['total']['away'])
                    setattr(selected_team, selected_columns[18], team_statistics['goals']['against']['total']['total'])
                    setattr(selected_team, selected_columns[19], team_statistics['goals']['against']['minute']), # JSON objec)
                    setattr(selected_team, selected_columns[20], team_statistics['biggest']['wins']['home'])
                    setattr(selected_team, selected_columns[21], team_statistics['biggest']['wins']['away'])
                    setattr(selected_team, selected_columns[22], team_statistics['biggest']['loses']['home'])
                    setattr(selected_team, selected_columns[23], team_statistics['biggest']['loses']['away'])
                    setattr(selected_team, selected_columns[24], team_statistics['clean_sheet']['home'])
                    setattr(selected_team, selected_columns[25], team_statistics['clean_sheet']['away'])
                    setattr(selected_team, selected_columns[26], team_statistics['clean_sheet']['total'])
                    setattr(selected_team, selected_columns[27], team_statistics['failed_to_score']['home'])
                    setattr(selected_team, selected_columns[28], team_statistics['failed_to_score']['away'])
                    setattr(selected_team, selected_columns[29], team_statistics['failed_to_score']['total'])
                    setattr(selected_team, selected_columns[30], team_statistics['penalty']['scored']['total'])
                    setattr(selected_team, selected_columns[31], team_statistics['penalty']['missed']['total'])
                    setattr(selected_team, selected_columns[32], team_statistics['cards']['yellow']), # JSON objec)
                    setattr(selected_team, selected_columns[33], team_statistics['cards']['red']), # JSON objec)

                    print('Dados do Time atualizados com sucesso')
                
                print('Erro ao buscar Time no Banco de Dados')

            else:
                print(f'Comunicação com endpoint Team Statistics falhou com código: {response.status_code}')
                break