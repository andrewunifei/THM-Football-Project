from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
import json
from collections import defaultdict

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
        games = g.db_session.query(game.Game).all()

        for instance in games:
            to_dict = model_to_dict(instance)
            translated = months_translation[instance.date.strftime("%B")]        
            periods[translated].append(to_dict)

        return jsonify(periods)