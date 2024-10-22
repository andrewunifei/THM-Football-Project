from flask import Flask, jsonify, request, g
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
# from models import *
from models import *

def venue_routes(app, Session):
    @app.before_request
    def before_request():
        """Create a new session before each request."""
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
        """Remove the session after each request."""
        Session.remove()

    @app.route('/top-cities', methods=['GET'])
    def get_top_cities():
        top_cities = (
            g.db_session.query(venue.Venue.city, func.count(venue.Venue.city).label('occurrence'))
            .group_by(venue.Venue.city)
            .order_by(func.count(venue.Venue.city).desc())
            .limit(5)
            .all()
        )
        return jsonify(dict(top_cities))

