from TomlPacker import TomlPacker
from YamlPacker import YamlPacker
from PicklePacker import PicklePacker
from JSONPacker import JsonPacker


class SerialiazeEnum:
    TOML = 1,
    JSON = 2,
    YAML = 3,
    PICKLE = 4


class Packer(object):
    @staticmethod
    def create_serializer(serialize_type):
        if serialize_type is SerialiazeEnum.YAML:
            return YamlPacker()
        if serialize_type is SerialiazeEnum.PICKLE:
            return PicklePacker()
        if serialize_type is SerialiazeEnum.TOML:
            return TomlPacker()
        if serialize_type is SerialiazeEnum.JSON:
            return JsonPacker()
