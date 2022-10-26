import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class JSONParser:
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "albumId": {"type": "number"},
                "url": {"type": "string"}
            },
            "required": [
                "title", "albumId", "url"
            ],
            "additionalProperties": True
        }
    }

    @classmethod
    def _is_json_valid(cls, json_data):
        try:
            validate(instance=json_data, schema=cls.schema)
            return True
        except ValidationError:
            return False

    @classmethod
    def import_from_url(cls, url: str):
        json_data = requests.get(url).json()
        if cls.is_json_valid(json_data):
            return json_data
        return False
