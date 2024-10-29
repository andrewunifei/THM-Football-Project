from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session, aliased
from models import *
import json
from collections import defaultdict
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
        data_dict = {}
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
        periods = {
            "Janeiro": list(),
            "Fevereiro": list(),
            "Março": list(),
            "Abril": list(),
            "Maio": list(),
            "Junho": list(),
            "Julho": list(),
            "Agosto": list(),
            "Setembro": list(),
            "Outubro": list(),
            "Novembro": list(),
            "Dezembro": list()
        }
        distinct_years_tuple =  g.db_session.query(func.extract('year', game.Game.date).label('year'))\
        .distinct().all()
        
        for year_tuple in distinct_years_tuple:
            periods_copy = copy.deepcopy(periods)
            home_team_alias = aliased(team.Team, name='home_team')
            away_team_alias = aliased(team.Team, name='away_team')
            # games = g.db_session.query(game.Game).where(func.extract('year', game.Game.date) == str(year_tuple[0])).all()
            games = g.db_session.query(game.Game)\
                .select_from(game.Game)\
                .join(home_team_alias, game.Game.home_team_id == home_team_alias.team_id)\
                .join(away_team_alias, game.Game.away_team_id == away_team_alias.team_id)\
                .where(func.extract('year', game.Game.date) == str(year_tuple[0]))\
                .add_columns(home_team_alias.name.label('home_team'), away_team_alias.name.label('away_team'))\
                .all()
            print(games)
            for instance in games:
                to_dict = model_to_dict(instance[0])
                translated = months_translation[instance[0].date.strftime("%B")]    
                to_dict['home_team'] = instance[1]    
                to_dict['away_team'] = instance[2]
                periods_copy[translated].append(to_dict)
            data_dict[str(year_tuple[0])] = periods_copy

            
        return jsonify(data_dict)
        #return ''