from psu1 import PSU
from flask import Flask, request
from flask_restful import Resource, Api

psu = PSU()

app = Flask(__name__)
api = Api(app)


class Voltage(Resource):
    def get(self):
        return psu.voltage

    def put(self):
        psu.voltage = request.form['data']
api.add_resource(Voltage, '/voltage')


class TurnOn(Resource):
    def put(self):
        psu.turn_on()
api.add_resource(TurnOn, '/turn_on')

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
