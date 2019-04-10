def get_api(cls):
    api = {'set': {},
           'get': {},
           'methods': {}
           }

    for name in dir(cls):
        if name.startswith('_'):
            continue

        attr = getattr(cls, name)
        if isinstance(attr, property):
            if attr.fget:
                api['get'][name] = attr.fget.__annotations__['return']
            if attr.fset:
                api['set'][name] = attr.fset.__annotations__['value']
        else:
            api['methods'][name] = {
                    'args': [],
                    'kwargs': {},
                    'return': attr.__annotations__.get('return')}
    return api
