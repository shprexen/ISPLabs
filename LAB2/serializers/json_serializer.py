import json
from .serializer import Serializer


class JsonPacker(Serializer):
    def dumps(self, obj):
        return json.dumps(super().dumps(obj), indent=4)

    def loads(self, string):
        return super().loads(json.loads(string))