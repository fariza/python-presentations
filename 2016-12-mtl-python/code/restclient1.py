import os
os.environ['no_proxy'] = 'localhost,127.0.0.1'
from requests import get, put


class PSU:
    def __init__(self, url='http://localhost:5000/'):
        self._url = url

    @property
    def voltage(self):
        return get(self._url + 'voltage').json()

    @voltage.setter
    def voltage(self, value):
        put(self._url + 'voltage', data={'data': value})

    def turn_on(self):
        put(self._url + 'turn_on')
