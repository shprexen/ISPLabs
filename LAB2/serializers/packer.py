from .yaml_serializer import YamlPacker
from .toml_serializer import TomlPacker
from .pickle_serializer import PicklePacker
from .json_serializer import JsonPacker


class SerialiazeEnum:
    TOML = 1,
    JSON = 2,
    YAML = 3,
    PICKLE = 4


class Packer(object):
    def create_serializer(serialize_type):
        if serialize_type == SerialiazeEnum.YAML:
            return YamlPacker()
        if serialize_type == SerialiazeEnum.PICKLE:
            return PicklePacker()
        if serialize_type == SerialiazeEnum.TOML:
            return TomlPacker()
        if serialize_type == SerialiazeEnum.JSON:
            return JsonPacker()
