from flask_restful import Resource
from mock_data import CLUBS

class ClubListResource(Resource):
    def get(self):
        return CLUBS, 200