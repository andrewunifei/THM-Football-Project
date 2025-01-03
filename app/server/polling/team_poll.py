from sqlalchemy import update
import requests
from models.team import Team

def handle_polling_team(engine, db_session, team_index, team_id):
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

    team_information_endpoint = f'teams?league={league}&season={season}&id={received_team_id}'
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
                stmt = (
                    update(Team)
                    .where(Team.team_id == team_id)
                    .values(**{
                        selected_columns[0]: team_data['fixtures']['played']['home'],
                        selected_columns[1]: team_data['fixtures']['played']['away'],
                        selected_columns[2]: team_data['fixtures']['played']['total'],
                        selected_columns[3]: team_data['fixtures']['wins']['home'],
                        selected_columns[4]: team_data['fixtures']['wins']['away'],
                        selected_columns[5]: team_data['fixtures']['wins']['total'],
                        selected_columns[6]: team_data['fixtures']['draws']['home'],
                        selected_columns[7]: team_data['fixtures']['draws']['away'],
                        selected_columns[8]: team_data['fixtures']['draws']['total'],
                        selected_columns[9]: team_data['fixtures']['loses']['home'],
                        selected_columns[10]: team_data['fixtures']['loses']['away'],
                        selected_columns[11]: team_data['fixtures']['loses']['total'],
                        selected_columns[12]: team_data['goals']['for']['total']['home'],
                        selected_columns[13]: team_data['goals']['for']['total']['away'],
                        selected_columns[14]: team_data['goals']['for']['total']['total'],
                        selected_columns[15]: team_data['goals']['for']['minute'],
                        selected_columns[16]: team_data['goals']['against']['total']['home'],
                        selected_columns[17]: team_data['goals']['against']['total']['away'],
                        selected_columns[18]: team_data['goals']['against']['total']['total'],
                        selected_columns[19]: team_data['goals']['against']['minute'],
                        selected_columns[20]: team_data['biggest']['wins']['home'],
                        selected_columns[21]: team_data['biggest']['wins']['away'],
                        selected_columns[22]: team_data['biggest']['loses']['home'],
                        selected_columns[23]: team_data['biggest']['loses']['away'],
                        selected_columns[24]: team_data['clean_sheet']['home'],
                        selected_columns[25]: team_data['clean_sheet']['away'],
                        selected_columns[26]: team_data['clean_sheet']['total'],
                        selected_columns[27]: team_data['failed_to_score']['home'],
                        selected_columns[28]: team_data['failed_to_score']['away'],
                        selected_columns[29]: team_data['failed_to_score']['total'],
                        selected_columns[30]: team_data['penalty']['scored']['total'],
                        selected_columns[31]: team_data['penalty']['missed']['total'],
                        selected_columns[32]: team_data['cards']['yellow'],
                        selected_columns[33]: team_data['cards']['red']
                    })
                )
                with engine.connect() as conn:
                    conn.execute(stmt)
                    conn.commit() 

                    print('Dados do Time atualizados com sucesso')
                

            else:
                print(f'Comunicação com endpoint Team Statistics falhou com código: {response.status_code}')
                break