import toml

"""def function_to_toml(func):
    members = inspect.getmembers(func.__code__)
    dickk = {}
    for item in members:
        if (item[0].startswith('co_')):
            dickk[item[0]] = item[1]
    dickk['co_code'] = list(dickk["co_code"])
    dickk['co_lnotab'] = list(dickk["co_lnotab"])
    return dickk"""


class TomlPacker:
    def dump(self, obj, fp):
        with open(fp, 'w') as file:
            toml.dump(obj, file)

    def dumps(self, obj):

        return toml.dumps(obj)

    def load(self, fp):
        return toml.load(fp)

    def loads(self, toml_string):
        return toml.loads(toml_string)
