from resources.club.clubList import ClubListResource
from resources.club.club import ClubResource
from flask_restful import Api
from flask import Flask

resource_config = [
    ClubListResource,
    ClubResource
]

def register_resources(api):
    for res in resource_config:
        args = (res.routes)
        
        api.add_resource(res, *args)