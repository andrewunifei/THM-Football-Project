from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func, or_
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
import json

def replace_none_with_zero(d):
    for key, value in d.items():
        if isinstance(value, dict):
            replace_none_with_zero(value)
        elif key in ['percentage', 'total'] and value is None:
            d[key] = 0 

def model_to_dict(instance):
    return {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

def team_routes(app, Session):
    CORS(app)
    
    @app.before_request
    def before_request():
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
        Session.remove()    

    @app.route('/teams/ids', methods=['GET'])
    def get_teams_id():
        ids = g.db_session.query(team.Team.team_id).all()
        to_list = [id_tuple[0] for id_tuple in ids]

        return jsonify(to_list)

    @app.route('/teams/info', methods=['GET'])
    def get_teams_info():
        teams =\
            g.db_session.query(team.Team.name, team.Team.code, team.Team.country, team.Team.founded, team.Team.logo)\
                        .where(team.Team.games_played_total > 0)\
                        .order_by(team.Team.name)\
                        .all()

        to_list = [
            {
                "name": name,
                "code": code,
                "country": country,
                "founded": founded,
                "logo": logo
            }
            for name, code, country, founded, logo in teams
        ]
        
        return jsonify(to_list)

    @app.route('/teams/games-info', methods=['GET'])
    def get_teams_games_info():
        keys = [
            'games_played_home',
            'games_played_away',
            'games_played_total',
            'wins_home',
            'wins_away',
            'wins_total',
            'losses_home',
            'losses_away',
            'losses_total',
            'draws_home',
            'draws_away',
            'draws_total'
        ]

        code = request.args.get('code')

        games_info_tuple =\
            g.db_session.query(
                team.Team.games_played_home, team.Team.games_played_away,\
                team.Team.games_played_total,\
                team.Team.wins_home, team.Team.wins_away, team.Team.wins_total,\
	            team.Team.losses_home, team.Team.losses_away, team.Team.losses_total,\
                team.Team.draws_home, team.Team.draws_away, team.Team.draws_total,)\
            .where(team.Team.games_played_total > 0, team.Team.code == code)\
            .first()

        if games_info_tuple:
            games_info_dict = dict(zip(keys, games_info_tuple))
            return jsonify(games_info_dict)
        else:
            return None

    @app.route('/teams/goals-info', methods=['GET'])
    def get_teams_goals_info():
        keys = [
            'goals_for_home',
            'goals_for_away',
            'goals_for_total',
            'segments_for',
            'goals_against_home',
            'goals_against_away',
            'goals_against_total',
            'segments_against',
            'biggest_win_home',
            'biggest_win_away',
            'biggest_loss_home',
            'biggest_loss_away',
        ]

        code = request.args.get('code')

        goals_info_tuple =\
            g.db_session.query(
                team.Team.goals_for_home, team.Team.goals_for_away,\
                team.Team.goals_for_total, team.Team.segments_for,\
                team.Team.goals_against_home, team.Team.goals_against_away,\
	            team.Team.goals_against_total, team.Team.segments_against,\
                team.Team.biggest_win_home, team.Team.biggest_win_away,\
                team.Team.biggest_loss_home, team.Team.biggest_loss_away)\
            .where(team.Team.games_played_total > 0, team.Team.code == code)\
            .first()

        if goals_info_tuple:
            goals_info_dict = dict(zip(keys, goals_info_tuple))
            return jsonify(goals_info_dict)
        else:
            return None
    
    @app.route('/teams/cards-info', methods=['GET'])
    def get_teams_cards_info():
        keys = [
            'yellow_cards',
            'red_cards',
        ]

        code = request.args.get('code')

        cards_info_tuple = \
            g.db_session.query(
                team.Team.yellow_cards,\
                team.Team.red_cards)\
            .where(team.Team.games_played_total > 0, team.Team.code == code)\
            .first()

        if cards_info_tuple:
            cards_info_dict = dict(zip(keys, cards_info_tuple))
            replace_none_with_zero(cards_info_dict)
            return jsonify(cards_info_dict)
        else:
            return None

    @app.route('/teams/match', methods=['GET'])
    def get_teams_match():
        result = []
        home_team_id = request.args.get('home_id')
        away_team_id = request.args.get('away_id')
        match_info_tuple = g.db_session.query(team.Team.team_id, team.Team.name)\
            .where(or_(team.Team.team_id == home_team_id, team.Team.team_id == away_team_id)).all()

        teams_dict = {team_id: name for team_id, name in match_info_tuple}

        return jsonify(teams_dict)
