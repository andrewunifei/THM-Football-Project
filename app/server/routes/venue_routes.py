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

    @app.route('/top-stadiums', methods=['GET'])
    def get_top_stadium():
        top_stadiums = []
        top_stadiums_objs =\
            g.db_session.query(venue.Venue)\
            .order_by(venue.Venue.capacity.desc())\
            .limit(5)\
            .all()
        for stadium_obj in top_stadiums_objs:
            del stadium_obj.__dict__['_sa_instance_state']
            top_stadiums.append(stadium_obj.__dict__)
        return jsonify(top_stadiums)