from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
import json
from collections import defaultdict

def model_to_dict(instance):
    return {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

def player_routes(app, Session):
    CORS(app)

    @app.before_request
    def before_request():
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
        Session.remove() 

    @app.route('/players-id', methods=['GET'])
    def get_players_id():
        ids = g.db_session.query(player.Player.player_id).all()
        to_list = [id_tuple[0] for id_tuple in ids]

        return jsonify(to_list)
    
    @app.route('/players/categorized', methods=['GET'])
    def get_players_categorized():
        keys = ['player_id', 'name', 'age', 'position', 'nationality', 'injured', 'photo', 'team', 'logo']

        data = (
            g.db_session.query(
                player.Player.player_id,
                player.Player.name,
                player.Player.age,
                player.Player.position,
                player.Player.nationality,
                player.Player.injured,
                player.Player.photo,
                team.Team.name.label('team'),
                team.Team.logo
            )
            .join(team.Team, player.Player.team_id == team.Team.team_id)
            .where(team.Team.games_played_total > 0)\
            .order_by(team.Team.name)
            .all()
        )

        data_dicts = [dict(zip(keys, case)) for case in data]

        grouped_teams = defaultdict(lambda: {"logo": "", "players": []})

        for player_info in data_dicts:
            team_key = player_info['team']
            
            if not grouped_teams[team_key]["logo"]:
                grouped_teams[team_key]["logo"] = player_info['logo']
        
            grouped_teams[team_key]["players"].append({
                'player_id': player_info['player_id'],
                'age': player_info['age'],
                'injured': player_info['injured'],
                'name': player_info['name'],
                'nationality': player_info['nationality'],
                'position': player_info['position'],
                'photo': player_info['photo']
            })

        categorized_by_team = []
        for team_key, data in grouped_teams.items():
            categorized_by_team.append({
                'team': team_key,
                'logo': data['logo'],
                'players': data['players']
            })

        return jsonify(categorized_by_team)

    @app.route('/players/player-info', methods=['GET'])
    def get_player_info():
        player_id = request.args.get('player-id')
        data = (
            g.db_session.query(player.Player)\
                .where(player.Player.player_id == player_id)
                .first()
        )

        player_dict = model_to_dict(data)

        return jsonify(player_dict)

    @app.route('/players/injuries', methods=['GET'])
    def get_player_info():
        player_id = request.args.get('player-id')
        result = (
            g.db_session.query(injury.Injury)
            .join(player.Player, injury.Injury.player_id == player.Player.player_id)
            .where(player.Player.player_id == player_id)
            .all()
        )

        print(result)

        return 'ok'