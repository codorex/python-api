from flask_restful import Resource, reqparse
from flask import request
from mock_data import CLUBS, CollectionWrapper

class ClubResource(Resource):
    def get(self, id):
        if id is None:
            return None

        clubsWrapper = CollectionWrapper(CLUBS)
        club = clubsWrapper.firstOrDefault(lambda i: i['id'] == id)

        if club is not None:
            return club, 200
        
        return None, 500

    def post(self):
        clubsWrapper = CollectionWrapper(CLUBS)
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('description')
        args = parser.parse_args()

        # TODO: validate if the request body contains
        # the required data

        largestId = clubsWrapper.max(lambda i: i['id'])

        club = {
            'id': largestId,
            'name': args['name'],
            'description': args['description']
        }

        CLUBS.append(club)

        return 'Created club with name ' + club['name'], 201