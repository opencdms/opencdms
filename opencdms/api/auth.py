from flask_jwt_extended import JWTManager


import os

from flask import Blueprint, jsonify, request
from flask_jwt_extended import verify_jwt_in_request, current_user
from flask_jwt_extended import create_access_token
import json


def rbac_route_protection_callback():
    # disable rbac by returning None
    # return None

    try:
        verify_jwt_in_request()
    except:
        user_role = 'anonymous'
    else:
        # Temporary: using usernames in rbac.json as role names
        # 
        user_role = current_user

    # Get the requested route and method
    requested_route_pattern = request.url_rule.rule
    requested_method = request.method
    
    # Load RBAC data
    file_path = os.path.join(os.path.dirname(__file__), 'rbac.json')
    with open(file_path, 'r') as rbac_file:
        rbac_data = json.load(rbac_file)

    # Get permissions for the user's role
    route_permissions = rbac_data.get(requested_route_pattern, {})
    role_permissions = route_permissions.get(user_role, {})

    # Check if the user is authorized to access the route
    if requested_method not in role_permissions:
        return jsonify({'message': 'Unauthorized'}), 403

    # User's role is authorized to access the route and method
    # Allow execution to continue to the view
    return None


def opencdms_auth(app):
    app.config["JWT_SECRET_KEY"] = "super-secret"  # TODO: Change this!
    jwt = JWTManager(app)
    # Register the route protection callback function as a "before_request" handler
    app.before_request(rbac_route_protection_callback)
