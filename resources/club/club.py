from flask_restful import Resource 
from flask import request
from flask.json import JSONDecoder
from mock_data import CLUBS, CollectionWrapper
from resources.routeMixin import RouteMixin

class ClubResource(Resource, RouteMixin):
    routes = [
        '/clubs',
        '/clubs/<int:id>'
    ]

    def get(self, id):
        if id is None:
            return None

        clubsWrapper = CollectionWrapper(CLUBS)
        club = clubsWrapper.firstOrDefault(lambda i: i['id'] == id)

        if club is not None:
            return club, 200
        
        return None, 500

    def post(self):
        return request.headers.__str__()
        club = request.get_json()
        clubsWrapper = CollectionWrapper(CLUBS)

        # TODO: validate if the request body contains
        # the required data

        largestId = clubsWrapper.max(lambda i: i['id'])

        club['id'] = largestId
        CLUBS.append(club)

        return 'Created club with name ' + club['name'], 201