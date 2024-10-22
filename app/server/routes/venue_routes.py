from flask import Flask, jsonify, request, g
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *

def venue_routes(app, Session):
    @app.before_request
    def before_request():
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
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
            first_key = list(stadium_obj.__dict__.keys())[0]
            del stadium_obj.__dict__[first_key]
            top_stadiums.append(stadium_obj.__dict__)
        return jsonify(top_stadiums)

    @app.route('/avg-capacity', methods=['GET'])
    def get_avg_capacity():
        avg_capacity = g.db_session.query(func.avg(venue.Venue.capacity)).scalar()        
        return format(avg_capacity, '.2f')

    @app.route('/surface-occurrences', methods=['GET'])
    def get_surface_occurrence():
        surface_occ =\
            g.db_session.query(venue.Venue.surface, func.count(venue.Venue.surface))\
            .group_by(venue.Venue.surface)\
            .all()
        return jsonify(dict(surface_occ))