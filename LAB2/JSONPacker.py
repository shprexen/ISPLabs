import json


class JsonPacker(object):
    def dump(self, obj, fp):
        with open(fp, 'w') as file:
            json.dump(json.dumps(obj.__dict__), fp)

    def dumps(self, obj):
        return json.dumps(obj.__dict__)

    def load(self, fp):
        with open(fp, 'w') as file:
            return json.load(file)

    def loads(self, data):
        return json.dumps(data)
