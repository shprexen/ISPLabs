import sys
import os
sys.path.insert(0, '/Serial/serializers')
from serializers import *


def choose(ext):
    if ext == '.json':
        return Packer.create_serializer(SerialiazeEnum.JSON)
    elif ext == '.yaml':
        return Packer.create_serializer(SerialiazeEnum.YAML)
    elif ext == '.pickle':
        return Packer.create_serializer(SerialiazeEnum.PICKLE)
    elif ext == '.toml':
        return Packer.create_serializer(SerialiazeEnum.TOML)


def get_ext(path):
    return os.path.splitext(path)[1]


def main():
    config_reader = Packer.create_serializer(SerialiazeEnum.JSON)
    config = config_reader.load('/home/shprexen/PycharmProjects/Serial/serializers/config.json')

    source_serializer = choose(get_ext(config['path']))
    obj = source_serializer.load(config['path'])
    target_serializer = choose(get_ext(config['target_file']))
    target_serializer.dump(obj, config['target_file'])


if __name__ == '__main__':
    main()
