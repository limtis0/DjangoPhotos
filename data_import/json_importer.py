import requests
from json import JSONDecodeError
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from .image_parser import ImageParser
from .url_is_valid import url_is_valid

from rest_framework.response import Response
from api.serializers import InputPhotoSerializer


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

    @classmethod
    def _import_json(cls, json_data):
        if not cls._is_json_valid(json_data):
            return Response('JSON response is invalid', status=400)

        driver = ImageParser.get_webdriver()
        for j in json_data[:10]:  # Restricted to 10 for demonstration
            serializer = InputPhotoSerializer(data=j)
            serializer.save_photo(driver)
        driver.close()

        return Response(status=200)

    @classmethod
    def import_from_url(cls, url: str):
        if not url_is_valid(url):
            return Response('Provided URL is invalid', status=400)

        try:
            json_data = requests.get(url).json()
        except JSONDecodeError:
            return Response('Could not parse JSON from provided URL', status=400)

        return cls._import_json(json_data)
