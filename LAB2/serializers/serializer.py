from types import FunctionType
from .converter import dict_to_function, function_to_dictionary, dict_to_object, primitive_to_dict, is_primitive


class Serializer:
    def dump(self, obj, fp):
        a = self.dumps(obj)
        with open(fp, 'w') as file:
            file.write(a)

    def dumps(self, obj):
        if type(obj) is FunctionType:
            obj_dict = function_to_dictionary(obj)
            return obj_dict
        if type(obj) is dict:
            return obj
        if is_primitive(obj):
            return primitive_to_dict(obj)
        else:
            obj = obj.__dict__
        return obj

    def load(self, fp):
        with open(fp, 'r') as file:
            return self.loads(file.read())

    def loads(self, obj):
        if 'globals' in obj.keys():
            return dict_to_function(obj)
        else:
            return dict_to_object(obj)
