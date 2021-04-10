import yaml
"""
def yaml_dumps(obj):
    dict_obj = obj.__dict__
    result = str()
    for key in dict_obj.keys():
        result += '\n' + key.__str__() + ':'
        if isinstance(dict_obj[key], Iterable):
            if isinstance(dict_obj[key], str):
                result += ' ' + dict_obj[key]
                continue
            for obj in list(dict_obj[key]):
                result += '\n- ' + str(obj)
        else:
            result += ' ' + str(dict_obj[key])
    return result
"""


class YamlPacker:
    def dump(self, obj, fp):
        with open(fp, 'w') as file:
            yaml.dump(obj, file)

    def dumps(self, obj):
        return yaml.dump(obj)

    def load(self, fp):
        with open(fp, 'r') as file:
            return yaml.unsafe_load(file)

    def loads(self, data):
        return yaml.unsafe_load(data)



