import json
import inspect
from types import CodeType, FunctionType

primitive_type = (int,
                  str,
                  float,
                  list,
                  tuple,
                  range,
                  dict,
                  set,
                  bool,
                  bytes)


def function_to_json(func):
    members = inspect.getmembers(func.__code__)
    dickk = {}
    for item in members:
        if (item[0].startswith('co_')):
            dickk[item[0]] = item[1]
    dickk['co_code'] = list(dickk["co_code"])
    dickk['co_lnotab'] = list(dickk["co_lnotab"])
    return dickk


def json_to_function(dickk):
    aue = CodeType(dickk['co_argcount'],
                   dickk['co_posonlyargcount'],
                   dickk['co_kwonlyargcount'],
                   dickk['co_nlocals'],
                   dickk['co_stacksize'],
                   dickk['co_flags'],
                   bytes(dickk['co_code']),
                   tuple(dickk['co_consts']),
                   tuple(dickk['co_names']),
                   tuple(dickk['co_varnames']),
                   dickk['co_filename'],
                   dickk['co_name'],
                   dickk['co_firstlineno'],
                   bytes(dickk['co_lnotab']),
                   tuple(dickk['co_freevars']),
                   tuple(dickk['co_cellvars']))
    func = FunctionType(aue, globals())
    return func


class JsonPacker(object):
    def dump(self, obj, fp):
        with open(fp, 'w') as file:
            if isinstance(obj, FunctionType):
                obj_dict = function_to_json(obj)
                file.write(json.dumps(obj_dict, indent=4))
            elif type(obj) in primitive_type:
                file.write(json.dumps(obj))
            else:
                file.write(self.dumps(obj))

    def dumps(self, obj):
        if isinstance(obj, FunctionType):
            obj_dict = function_to_json(obj)
            return json.dumps(obj_dict, indent=2)
        elif type(obj) in primitive_type:
            return json.dumps(obj)
        else:
            return json.dumps(obj, default=lambda x: x.__dict__, sort_keys=True, indent=4)

    def load(self, fp):
        obj_dict = {}
        with open(fp, 'r') as file:
            obj_dict = json.loads(file.read())
            try:
                if "co_firstlineno" in obj_dict.keys():
                    return json_to_function(obj_dict)
                else:
                    with open(fp, 'r') as f:
                        return json.loads(f.read())
            except:
                with open(fp, 'r') as f:
                    return self.loads(f.read())

    def loads(self, data):
        obj_dict = json.loads(data)
        try:
            if "co_firstlineno" in obj_dict.keys():
                return json_to_function(obj_dict)
            else:
                json.loads(data)
        except:
            return json.loads(data)
