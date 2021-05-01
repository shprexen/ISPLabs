import sys
sys.path.insert(0, '/home/shprexen/PycharmProjects/Serial/')

import unittest
from serializers.packer import *
from test_objects import *


class TestPacker(unittest.TestCase):
    def setUp(self):
        self.serializer = Packer.create_serializer(SerialiazeEnum.JSON)
        self.obj = TestObjects()
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.json'

    def test_function_json(self):
        self.serializer.dump(func, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(), func())

    def test_recursion_json(self):
        self.serializer.dump(fibonacci, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(6), fibonacci(6))

    def test_primitives_json(self):
        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))
        test_num = self.serializer.loads(self.serializer.dumps(self.obj.num))
        test_list = self.serializer.loads(self.serializer.dumps(self.obj.list))
        test_string = self.serializer.loads(self.serializer.dumps(self.obj.string))

        self.assertEqual(self.obj.dict, test_dict)
        self.assertEqual(self.obj.num, test_num)
        self.assertEqual(self.obj.string, test_string)
        self.assertEqual(self.obj.list, test_list)

    def test_lambda_json(self):
        json_obj = self.serializer.loads(self.serializer.dumps(lam_func))
        self.assertEqual(json_obj(6), lam_func(6))

    def test_primitives_pickle(self):
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.pickle'
        self.serializer = Packer.create_serializer(SerialiazeEnum.PICKLE)

        self.serializer.dump(func, self.fp)
        test_obj = self.serializer.load(self.fp)
        self.assertEqual(test_obj, func)

        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))
        test_num = self.serializer.loads(self.serializer.dumps(self.obj.num))
        test_list = self.serializer.loads(self.serializer.dumps(self.obj.list))
        test_string = self.serializer.loads(self.serializer.dumps(self.obj.string))

        self.assertEqual(self.obj.dict, test_dict)
        self.assertEqual(self.obj.num, test_num)
        self.assertEqual(self.obj.string, test_string)
        self.assertEqual(self.obj.list, test_list)

    def test_class_object_pickle(self):
        self.serializer = Packer.create_serializer(SerialiazeEnum.PICKLE)
        self.serializer.dump(test_object, self.fp)
        _obj = self.serializer.load(self.fp)
        self.assertEqual(_obj.string, test_object.string)

    def test_function_pickle(self):
        self.serializer.dump(func, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(), func())

    def test_recursion_pickle(self):
        self.serializer.dump(func, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(), func())

    def test_lambda_pickle(self):
        pickle_obj = self.serializer.loads(self.serializer.dumps(lam_func))
        self.assertEqual(pickle_obj(6), lam_func(6))

    def test_primitives_yaml(self):
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.yaml'
        self.serializer = Packer.create_serializer(SerialiazeEnum.YAML)

        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))
        test_num = self.serializer.loads(self.serializer.dumps(self.obj.num))
        test_list = self.serializer.loads(self.serializer.dumps(self.obj.list))
        test_string = self.serializer.loads(self.serializer.dumps(self.obj.string))
        self.assertEqual(self.obj.dict, test_dict)
        self.assertEqual(self.obj.num, test_num)
        self.assertEqual(self.obj.string, test_string)
        self.assertEqual(self.obj.list, test_list)

    def test_class_object_yaml(self):
        self.serializer = Packer.create_serializer(SerialiazeEnum.YAML)
        self.serializer.dump(test_object, self.fp)
        _obj = self.serializer.load(self.fp)
        self.assertEqual(_obj.string, test_object.string)

    def test_function_yaml(self):
        self.serializer.dump(func, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(), func())

    def test_recursion_yaml(self):
        self.serializer.dump(fibonacci, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(6), fibonacci(6))

    def test_lambda_yaml(self):
        yaml_obj = self.serializer.loads(self.serializer.dumps(lam_func))
        self.assertEqual(yaml_obj(6), lam_func(6))

    def test_primitives_toml(self):
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.toml'
        self.serializer = Packer.create_serializer(SerialiazeEnum.TOML)

        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))
        test_num = self.serializer.loads(self.serializer.dumps(self.obj.num))
        test_list = self.serializer.loads(self.serializer.dumps(self.obj.list))
        test_string = self.serializer.loads(self.serializer.dumps(self.obj.string))
        self.assertEqual(self.obj.dict, test_dict)
        self.assertEqual(self.obj.num, test_num)
        self.assertEqual(self.obj.string, test_string)
        self.assertEqual(self.obj.list, test_list)

    def test_function_toml(self):
        self.serializer.dump(func, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(), func())

    def test_recursion_toml(self):
        self.serializer.dump(fibonacci, self.fp)
        test_func = self.serializer.load(self.fp)
        self.assertEqual(test_func(6), fibonacci(6))


    def test_lambda_toml(self):
        toml_obj = self.serializer.loads(self.serializer.dumps(lam_func))
        self.assertEqual(toml_obj(6), lam_func(6))


if __name__ == "__main__":
    unittest.main()
