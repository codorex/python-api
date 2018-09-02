from flask_restful import Resource
from mock_data import CLUBS
from resources.routeMixin import RouteMixin
class ClubListResource(Resource, RouteMixin):
    routes = [
        '/clubs'
    ]

    def get(self):
        return CLUBS, 200