import builtins
import json
import inspect
from types import CodeType, FunctionType


def is_primitive(obj):
    return type(obj) in [int, float, str, bool, type(None), list, tuple]


def function_to_json(obj):
    members = inspect.getmembers(obj.__code__)
    func_dict = {}
    for item in members:
        if item[0].startswith('co_'):
            func_dict[item[0]] = item[1]
    func_dict['co_code'] = list(func_dict["co_code"])
    func_dict['co_lnotab'] = list(func_dict["co_lnotab"])

    func = {'code': func_dict}

    function_globals = dict()
    name = func['code']['co_name']
    function_globals[name] = name + '<function>'
    global_pairs = obj.__globals__.items()
    for (key, value) in global_pairs:
        if is_primitive(value):
            function_globals[key] = value
    func['globals'] = function_globals
    return func


def json_to_function(dict_func):
    function_globals = dict_func['globals']
    function_globals['__builtins__'] = builtins
    code_args = dict_func['code']

    my_obj = CodeType(code_args['co_argcount'],
                   code_args['co_posonlyargcount'],
                   code_args['co_kwonlyargcount'],
                   code_args['co_nlocals'],
                   code_args['co_stacksize'],
                   code_args['co_flags'],
                   bytes(code_args['co_code']),
                   tuple(code_args['co_consts']),
                   tuple(code_args['co_names']),
                   tuple(code_args['co_varnames']),
                   code_args['co_filename'],
                   code_args['co_name'],
                   code_args['co_firstlineno'],
                   bytes(code_args['co_lnotab']),
                   tuple(code_args['co_freevars']),
                   tuple(code_args['co_cellvars']))

    temp = FunctionType(my_obj, function_globals, code_args['co_name'])
    name = code_args['co_name']
    function_globals[name] = temp
    return FunctionType(my_obj, function_globals, name)


class JsonPacker(object):
    def dump(self, obj, fp):
        with open(fp, 'w') as file:
            if isinstance(obj, FunctionType):
                obj_dict = function_to_json(obj)
                file.write(json.dumps(obj_dict, indent=4))
            elif is_primitive(obj):
                file.write(json.dumps(obj))
            else:
                file.write(self.dumps(obj))

    def dumps(self, obj):
        if isinstance(obj, FunctionType):
            obj_dict = function_to_json(obj)
            return json.dumps(obj_dict, indent=2)
        elif is_primitive(obj):
            return json.dumps(obj)
        else:
            return json.dumps(obj, default=lambda x: x.__dict__, sort_keys=True, indent=4)

    def load(self, fp):
        obj_dict = {}
        with open(fp, 'r') as file:
            obj_dict = json.loads(file.read())
            try:
                if "code" in obj_dict.keys():
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
                return json.loads(data)
        except:
            return json.loads(data)
