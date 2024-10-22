# routes.py
from flask import Blueprint, jsonify, request

# Create a Blueprint for routes
api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    # Logic to fetch users
    return jsonify({"users": []})

@api.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Logic to fetch a specific user by ID
    return jsonify({"user": {"id": user_id}})

@api.route('/users', methods=['POST'])
def create_user():
    data = request.json  # Get JSON data from request
    # Logic to create a new user
    return jsonify({"message": "User created!"}), 201