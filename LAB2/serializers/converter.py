import inspect
import builtins
from types import CodeType, FunctionType


def is_primitive(obj):
    return type(obj) in [int, float, str, bool, type(None), list, tuple]


def function_to_dictionary(obj):
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


def dict_to_function(dict_func):
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


def primitive_to_dict(obj):
    obj_dict = {}
    if type(obj) is list:
        i = 1
        for item in obj:
            obj_dict["Variable" + str(i)] = item
            i += 1
        return obj_dict
    if type(obj) is dict:
        return obj
    if is_primitive(obj):
        obj_dict["Variable"] = obj
    else:
        obj_dict = obj.__dict__
    return obj_dict


def dict_to_object(obj_dict):
    if "Variable" in obj_dict.keys():
        return obj_dict["Variable"]
    if "Variable1" in obj_dict.keys():
        l = []
        for key in obj_dict.keys():
            l.append(obj_dict[key])
        return l
    if type(obj_dict) is dict:
        return obj_dict
