import requests
import json
from models import *

# Esses dados são referentes a entidade 'Time' no diagrama ER
def fetch_team_and_populate(api_key, league, season, db_session):
    if True:
        data = {}
        with open('../../teams_first_half.json', 'r') as file:
            data = json.load(file)
        number_of_results = data['results']
        team_data = data['response'][0]

        # Inserindo dados no banco de dados
        for key, value in team_data.items(): 
            if team_data[key] is None: 
                    team_data[key] = 0

        teams_statistics = {}
        with open('../../teams_second_half.json', 'r') as file2:
            data2 = json.load(file2)
        team_statistics = data2['response']

        if type(team_statistics) == list:
            return
        else:
            new_team = team.Team(
                team_id=team_data['team']['id'],
                name=team_data['team']['name'],
                code=team_data['team']['code'],
                country=team_data['team']['country'],
                founded=team_data['team']['founded'],
                national=team_data['team']['national'],
                logo=team_data['team']['logo'],
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
                venue_id=team_data['venue']['id']
            )
            db_session.add(new_team)

    db_session.commit()