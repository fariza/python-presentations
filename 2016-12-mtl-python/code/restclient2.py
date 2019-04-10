import os
import json
os.environ['no_proxy'] = 'localhost,127.0.0.1'
from requests import get, put


class PSU:
    def __init__(self, url='http://localhost:5000/'):
        self._url = url
        self._api = json.loads(self._get('api'))
        self._add_properties(self._api)
        self._add_methods(self._api)

    def _get(self, attr):
        return get(self._url + attr).json()

    def _put(self, attr, value):
        put(self._url + attr, data={'data': value})

    def _call(self, attr, *args, **kwargs):
        return put(self._url + attr, data={'args': args,
                                           'kwargs': kwargs})

    @classmethod
    def _add_properties(cls, api):
        for attr in api['get'].keys():
            def fget(self):
                return self._get(attr)

            def fset(self, value):
                self._put(attr, value)
            setattr(cls, attr, property(fget, fset))

    @classmethod
    def _add_methods(cls, api):
        for attr in api['methods'].keys():
            def method(self):
                self._call(attr)
            setattr(cls, attr, method)
