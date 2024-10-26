from flask import Flask, jsonify, request, g
from flask_cors import CORS
from sqlalchemy import create_engine, inspect, func
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *
import pandas as pd

def venue_routes(app, Session):
    CORS(app)
    
    @app.before_request
    def before_request():
        g.db_session = Session()

    @app.teardown_request
    def teardown_request(exception):
        Session.remove()

    @app.route('/venues-id', methods=['GET'])
    def get_venue_ids():
        ids = g.db_session.query(venue.Venue.venue_id).all()
        to_list = [id_tuple[0] for id_tuple in ids]

        return jsonify(to_list)

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
            .limit(3)\
            .all()
        for stadium_obj in top_stadiums_objs:
            first_key = list(stadium_obj.__dict__.keys())[0]
            del stadium_obj.__dict__[first_key]
            top_stadiums.append(stadium_obj.__dict__)
        return jsonify(top_stadiums)

    @app.route('/bottom-stadiums', methods=['GET'])
    def get_bottom_stadium():
        bottom_stadiums = []
        bottom_stadiums_objs =\
            g.db_session.query(venue.Venue)\
            .order_by(venue.Venue.capacity.asc())\
            .limit(3)\
            .all()
        for stadium_obj in bottom_stadiums_objs:
            first_key = list(stadium_obj.__dict__.keys())[0]
            del stadium_obj.__dict__[first_key]
            bottom_stadiums.append(stadium_obj.__dict__)
        return jsonify(bottom_stadiums)

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

    @app.route('/capacities-categorized', methods=['GET'])
    def get_capacities_categorized():
        tuple_capacities = \
            g.db_session.query(venue.Venue.capacity).order_by(venue.Venue.capacity.asc()).all()

        data = [item[0] for item in tuple_capacities]

        interval = 5000
        
        # Convert the list to a DataFrame
        df = pd.DataFrame(data, columns=['capacity'])
        
        # Define the intervals (bins)
        bins = range(0, max(data) + interval, interval)
        
        # Categorize the data into bins and count occurrences
        df['interval'] = pd.cut(df['capacity'], bins=bins)
        counts = df['interval'].value_counts().sort_index()
        
        # Prepare result for JSON response
        result = counts.reset_index()
        result.columns = ['interval', 'count']
        result['interval'] = result['interval'].astype(str)
        
        return jsonify(result.to_dict(orient='records'))