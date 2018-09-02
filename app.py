from flask_restful import Resource, reqparse, Api
from flask import Flask
from routes import register_resources

app = Flask(__name__)
api = Api(app)

register_resources(api)

app.run(debug=True)
