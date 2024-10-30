from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func, and_
from sqlalchemy.orm import sessionmaker, scoped_session, aliased
from models import *
import json
from collections import defaultdict, namedtuple
import copy


def model_to_dict(instance):
    return {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

def game_routes(app, Session):
    CORS(app)

    @app.before_request
    def before_request():
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
        Session.remove() 

    @app.route('/games-id', methods=['GET'])
    def get_games_id():
        ids = g.db_session.query(game.Game.game_id).all()
        to_list = [id_tuple[0] for id_tuple in ids]

        return jsonify(to_list)
    
    @app.route('/games/categorized', methods=['GET'])
    def get_games():
        data = []
        months_translation = {
            "January": "Janeiro",
            "February": "Fevereiro",
            "March": "Março",
            "April": "Abril",
            "May": "Maio",
            "June": "Junho",
            "July": "Julho",
            "August": "Agosto",
            "September": "Setembro",
            "October": "Outubro",
            "November": "Novembro",
            "December": "Dezembro"
        }
        year = request.args.get('year')
        month = request.args.get('month')

    
        home_team_alias = aliased(team.Team, name='home_team')
        away_team_alias = aliased(team.Team, name='away_team')
        # games = g.db_session.query(game.Game).where(func.extract('year', game.Game.date) == str(year_tuple[0])).all()
        games = g.db_session.query(game.Game)\
            .select_from(game.Game)\
            .join(home_team_alias, game.Game.home_team_id == home_team_alias.team_id)\
            .join(away_team_alias, game.Game.away_team_id == away_team_alias.team_id)\
            .filter(and_(func.extract('year', game.Game.date) == year , func.extract('month', game.Game.date) == month))\
            .add_columns(home_team_alias.name.label('home_team'), away_team_alias.name.label('away_team'))\
            .all()
        # print(games)

        for instance in games:
            to_dict = model_to_dict(instance[0])
            translated = months_translation[instance[0].date.strftime("%B")]    
            to_dict['home_team'] = instance[1]    
            to_dict['away_team'] = instance[2]
            data.append(to_dict)

        return jsonify(data)
        #return ''

    @app.route('/games/available', methods=['GET'])
    def get_games_available():
        by_year = {}
        months = []
        games_available = g.db_session.query(
            func.extract('month', game.Game.date).label('months'),
            func.extract('year', game.Game.date).label('years')
        )\
        .distinct()\
        .order_by(func.extract('month', game.Game.date))\
        .all()

        for available in games_available:
            by_year[str(available[1])] = []
        
        for available in games_available:
            by_year[str(available[1])].append(available[0])

        return jsonify(by_year)

    @app.route('/games/details', methods=['GET'])
    def get_games_details():
        game_id = request.args.get('game-id')

        home_team_alias = aliased(team.Team, name='home_team')
        away_team_alias = aliased(team.Team, name='away_team')
        games_details = g.db_session.query(
            game.Game,
            home_team_alias.name.label('home_name'),
            home_team_alias.code.label('home_code'),
            home_team_alias.logo.label('home_logo'),
            away_team_alias.name.label('away_name'),
            away_team_alias.code.label('away_code'),
            away_team_alias.logo.label('away_logo'),
            venue.Venue.image.label('stadium_photo'),
            venue.Venue.name.label('stadium_name'),
            venue.Venue.address.label('stadium_address'),
            venue.Venue.city.label('city'),
            venue.Venue.capacity.label('stadium_capacity'),

        )\
        .join(home_team_alias, game.Game.home_team_id == home_team_alias.team_id)\
        .join(away_team_alias, game.Game.away_team_id == away_team_alias.team_id)\
        .join(venue.Venue, game.Game.venue_id == venue.Venue.venue_id)\
        .filter(game.Game.game_id == game_id)\
        .first()

        to_dict = model_to_dict(games_details[0])    
        game_data_dict = {
            'game': to_dict,
            'home_name': games_details.home_name,
            'home_code': games_details.home_code,
            'home_logo': games_details.home_logo,
            'away_name': games_details.away_name,
            'away_code': games_details.away_code,
            'away_logo': games_details.away_logo,
            'stadium_photo': games_details.stadium_photo,
            'stadium_name': games_details.stadium_name,
            'stadium_address': games_details.stadium_address,
            'city': games_details.city,
            'stadium_capacity': games_details.stadium_capacity
        }

        return jsonify(game_data_dict)