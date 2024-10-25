from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
import json

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