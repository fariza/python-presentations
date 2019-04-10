from psu2 import PSU
from flask import Flask, request
from flask_restful import Resource, Api
from extractor import get_api
import json

psu = PSU()
d_api = get_api(PSU)
app = Flask(__name__)
api = Api(app)


class TypeAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            r = json.JSONEncoder.default(self, obj)
        except TypeError:
            r = obj.__name__
        return r


class DApi(Resource):
    def get(self):
        return json.dumps(d_api, cls=TypeAwareJSONEncoder)
api.add_resource(DApi, '/api')


class RestPSU(Resource):
    def get(self, attr):
        return getattr(psu, attr)

    def put(self, attr):
        if attr in d_api['set']:
            value = d_api['set'][attr](request.form['data'])
            setattr(psu, attr, value)
        elif attr in d_api['methods']:
            getattr(psu, attr)()

api.add_resource(RestPSU, '/<string:attr>')


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
