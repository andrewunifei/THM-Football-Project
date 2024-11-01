from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
import pandas as pd
import json

def fake_server(app):
    @app.route('/fake/games', methods=['GET'])
    def get_fake_game():
        with open('game_fake_data.json', 'r') as file:
            data = json.load(file)

        return jsonify(data)

    @app.route('/fake/teams', methods=['GET'])
    def get_fake_team():
        index = request.args.get('index')
        with open('team_fake_data.json', 'r') as file:
            data = json.load(file)

        return jsonify(data[int(index)])

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    fake_server(app)
    app.run(debug=True, port=8080)
