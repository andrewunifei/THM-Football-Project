from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
import json

def instance_to_dict(instance):
    return {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

def team_routes(app, Session):
    CORS(app)
    
    @app.before_request
    def before_request():
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
        Session.remove()

    @app.route('/teams-info', methods=['GET'])
    def get_teams_info():
        teams =\
            g.db_session.query(team.Team.name, team.Team.code, team.Team.country, team.Team.founded, team.Team.logo)\
                        .where(team.Team.games_played_total > 0)\
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

    @app.route('/teams-games-info', methods=['GET'])
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
