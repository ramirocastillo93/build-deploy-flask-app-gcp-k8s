from flask import Blueprint, request
from services.user_service import get_user_service, put_user_service

user_route = Blueprint('user_route', __name__)

@user_route.route('/hello/<username>', methods=['GET'])
def hello_world_get(username):
    return get_user_service(username)

@user_route.route('/hello/<username>', methods=['PUT'])    
def hello_world_put(username):
    return put_user_service(username, request)