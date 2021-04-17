import unittest
from types import FunctionType
from Packer import Packer, SerialiazeEnum
from TestObjects import TestObjects, func, fibonacci


class TestPacker(unittest.TestCase):
    def setUp(self):
        self.serializer = Packer.create_serializer(SerialiazeEnum.JSON)
        self.obj = TestObjects()
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.json'

    def test_primitives_json(self):
        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))
        test_num = self.serializer.loads(self.serializer.dumps(self.obj.num))
        test_list = self.serializer.loads(self.serializer.dumps(self.obj.list))
        test_string = self.serializer.loads(self.serializer.dumps(self.obj.string))

        self.assertEqual(self.obj.dict, test_dict)
        self.assertEqual(self.obj.num, test_num)
        self.assertEqual(self.obj.string, test_string)
        self.assertEqual(self.obj.list, test_list)

    def test_function_json(self):
        self.serializer.dump(func, self.fp)
        self.assertIsInstance(self.serializer.load(self.fp), FunctionType)

    def test_recursion_json(self):
        self.serializer.dump(fibonacci, self.fp)
        self.assertIsInstance(self.serializer.load(self.fp), FunctionType)

    def test_primitives_pickle(self):
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.pickle'
        self.serializer = Packer.create_serializer(SerialiazeEnum.PICKLE)

        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))
        test_num = self.serializer.loads(self.serializer.dumps(self.obj.num))
        test_list = self.serializer.loads(self.serializer.dumps(self.obj.list))
        test_string = self.serializer.loads(self.serializer.dumps(self.obj.string))

        self.assertEqual(self.obj.dict, test_dict)
        self.assertEqual(self.obj.num, test_num)
        self.assertEqual(self.obj.string, test_string)
        self.assertEqual(self.obj.list, test_list)

    def test_function_pickle(self):
        self.serializer.dump(func, self.fp)
        self.assertIsInstance(self.serializer.load(self.fp), FunctionType)

    def test_recursion_pickle(self):
        self.serializer.dump(fibonacci, self.fp)
        self.assertIsInstance(self.serializer.load(self.fp), FunctionType)

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

    def test_function_yaml(self):
        self.serializer.dump(func, self.fp)
        self.assertIsInstance(self.serializer.load(self.fp), FunctionType)

    def test_recursion_yaml(self):
        self.serializer.dump(fibonacci, self.fp)
        self.assertIsInstance(self.serializer.load(self.fp), FunctionType)



    def test_toml(self):
        self.fp = '/home/shprexen/PycharmProjects/Serial/Files/file.toml'
        self.serializer = Packer.create_serializer(SerialiazeEnum.TOML)

        self.serializer.dump(self.obj.dict, self.fp)
        self.assertEqual(self.serializer.load(self.fp), self.obj.dict)

        test_dict = self.serializer.loads(self.serializer.dumps(self.obj.dict))

        self.assertEqual(self.obj.dict, test_dict)


if __name__ == "__main__":
    unittest.main()
