from flask import Flask, jsonify, request, g
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models.venue import Venue

def venue_routes(app, Session):
    @app.before_request
    def before_request():
        """Create a new session before each request."""
        g.db_session = Session()

    # @app.teardown_request
    # def teardown_request(exception):
    #     """Remove the session after each request."""
    #     Session.remove()

    @app.route('/top-cities', methods=['GET'])
    def get_top_cities():
        top_cities = (
            g.db_session.query(Venue.city, func.count(Venue.city).label('occurrence'))
            .group_by(Venue.city)
            .order_by(func.count(Venue.city).desc())
            .limit(5)
            .all()
        )
        return jsonify(dict(top_cities))

