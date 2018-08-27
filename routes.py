from resources.club.clubList import ClubListResource
from resources.club.club import ClubResource
from flask_restful import Api
from flask import Flask

route_config = [
    {
        'resource': ClubListResource, 
        'routes': ["/clubs"]
    },
    {
        'resource': ClubResource,
        'routes': ["/club", "/club/<int:id>"]
    }
]

def register_routes(api):
    for route in route_config:
        args = (route['routes'])
        
        api.add_resource(route['resource'], *args)