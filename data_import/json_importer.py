import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework.response import Response
from image_parser import ImageParser


class JSONImporter:
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

    @staticmethod
    def import_from_url(url: str):
        return requests.get(url).json()

    @classmethod
    def _import_json(cls, json_data):
        if not cls._is_json_valid(json_data):
            return Response('JSON answer is invalid')

        driver = ImageParser.get_webdriver()
        for j in json_data:
            pass

        driver.close()
