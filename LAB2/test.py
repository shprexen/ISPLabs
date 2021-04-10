import yaml
import pickle
import inspect
import toml
from types import CodeType, FunctionType


class Class(object):
    def __init__(self):
        self.a = 'dfsdfsd'

    def xui(self):
        pass


def func(a, b):
    a = 7
    print(a + b)


def fun_to_YAML(fun):
    func_name = func.__code__.co_name
    func_args = func.__code__.co_varnames
    str = 'FunctionName: ' + func_name
    str = str + '\nArguments:'
    for i in range(len(func_args)):
        str += '\n- ' + func_args[i]
    return str


def fun_to_json(fun):
    func__code = inspect.getsourcelines(fun)
    func_name = func.__code__.co_name
    func_args = func.__code__.co_varnames
    str = '{"FunctionName:"' + ' "{}"'.format(func_name)
    str += ', "Arguments": ['
    for i in range(len(func_args)):
        if i != (len(func_args) - 1):
            str += '{}, '.format(func_args[i])
        else:
            str += '{}'.format(func_args[i])
    str += ', "Function code: ' + func__code
    str += ']}'

    return str


def fun_to_pickle(func, fp):
    with open('fp', 'wb') as file:
        pickle.dump(func, file)


def func_to_yaml(func):
    func_name = func.__code__.co_name
    func_args = func.__code__.co_varnames
    str = 'FunctionName: ' + func_name
    str = str + '\nArguments:'
    for i in range(len(func_args)):
        str += '\n- ' + func_args[i]
    return str


def f(a, b, c):
    g = a + b ** c
    return g


a = Class()

print(toml.dumps(a))
