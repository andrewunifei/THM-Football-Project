import requests
from ..models.team import Team 

# Esses dados são referentes a entidade 'Time' no diagrama ER
def fetch_team_and_populate(api_key, league, season, db_session):
    team_information_endpoint = f'teams?league={league}&season={season}'
    api_url = f'https://v3.football.api-sports.io/{team_information_endpoint}'
    headers = {
        'x-rapidapi-host': 'v3.football.api-sports.io',
        'x-rapidapi-key': api_key
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        teams_data = response.json()
        number_of_results = teams_data['results']
        print(teams_data)

        # Inserindo dados no banco de dados
        for team in teams_data['response']:
            for key, value in team.items(): 
                if team[key] is None: 
                        team[key] = 0

            team_statistics = {}
            team_id = team['team']['id']
            team_statistics_endpoint = f'teams/statistics?league={league}&season={season}&team={team_id}'
            api_url = f'https://v3.football.api-sports.io/{team_statistics_endpoint}'
            response = requests.get(api_url, headers=headers)

            if response.status_code == 200:
                team_statistics = response.json()
                team_statistics = team_statistics['response']
            else:
                print(f"Comunicação com endpoint Team Statistics falhou com código: {response.status_code}")
                break

            if type(team_statistics) == list:
                continue

            new_team = Team(
                team_id=team['team']['id'],
                name=team['team']['name'],
                code=team['team']['code'],
                country=team['team']['country'],
                founded=team['team']['founded'],
                national=team['team']['national'],
                logo=team['team']['logo'],
                games_played_home=team_statistics['fixtures']['played']['home'],
                games_played_away=team_statistics['fixtures']['played']['away'],
                games_played_total=team_statistics['fixtures']['played']['total'],
                wins_home=team_statistics['fixtures']['wins']['home'],
                wins_away=team_statistics['fixtures']['wins']['away'],
                wins_total=team_statistics['fixtures']['wins']['total'],
                draws_home=team_statistics['fixtures']['draws']['home'],
                draws_away=team_statistics['fixtures']['draws']['away'],
                draws_total=team_statistics['fixtures']['draws']['total'],
                losses_home=team_statistics['fixtures']['loses']['home'],
                losses_away=team_statistics['fixtures']['loses']['away'],
                losses_total=team_statistics['fixtures']['loses']['total'],
                goals_for_home=team_statistics['goals']['for']['total']['home'],
                goals_for_away=team_statistics['goals']['for']['total']['away'],
                goals_for_total=team_statistics['goals']['for']['total']['total'],
                segments_for=team_statistics['goals']['for']['minute'], # JSON object
                goals_against_home=team_statistics['goals']['against']['total']['home'],
                goals_against_away=team_statistics['goals']['against']['total']['away'],
                goals_against_total=team_statistics['goals']['against']['total']['total'],
                segments_against=team_statistics['goals']['against']['minute'], # JSON object
                biggest_win_home=team_statistics['biggest']['wins']['home'],
                biggest_win_away=team_statistics['biggest']['wins']['away'],
                biggest_loss_home=team_statistics['biggest']['loses']['home'],
                biggest_loss_away=team_statistics['biggest']['loses']['away'],
                clean_sheet_home=team_statistics['clean_sheet']['home'],
                clean_sheet_away=team_statistics['clean_sheet']['away'],
                clean_sheet_total=team_statistics['clean_sheet']['total'],
                failed_to_score_home=team_statistics['failed_to_score']['home'],
                failed_to_score_away=team_statistics['failed_to_score']['away'],
                failed_to_score_total=team_statistics['failed_to_score']['total'],
                penalty_scored=team_statistics['penalty']['scored']['total'],
                penalty_missed=team_statistics['penalty']['missed']['total'],
                yellow_cards=team_statistics['cards']['yellow'], # JSON object
                red_cards=team_statistics['cards']['red'], # JSON object
                venue_id=team['venue']['id']
            )
            db_session.add(new_team)

        db_session.commit()
        print("Dados inseridos com sucesso.")

    else:
        print(f"Comunicação com a API falhou com código: {response.status_code}")