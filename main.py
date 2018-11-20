import time

from flask import Flask

from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class HealthCheck(Resource):
    def get(self):
        return {'ping': time.time()}

api.add_resource(HelloWorld, '/')
api.add_resource(HealthCheck, '/ping')

if __name__ == '__main__':
    app.run(debug=True)
