from flask_restful import Resource, reqparse, Api
from flask import Flask
from routes import register_routes

app = Flask(__name__)
api = Api(app)

register_routes(api)

app.run(debug=True)
