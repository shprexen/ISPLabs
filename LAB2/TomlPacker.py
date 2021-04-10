import toml


class TomlPacker(object):
    def dump(self, obj, fp):

        with open(fp, 'w') as file:
            toml.dump(obj.__dict__, file)

    def dumps(self, obj):
        return toml.dumps(obj.__dict__)

    def load(self, fp):
        with open(fp, 'r') as file:
            return toml.load(file)

    def loads(self, data):
        return toml.loads(data)
