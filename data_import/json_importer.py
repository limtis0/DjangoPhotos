import json
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from .url_is_valid import url_is_valid

from rest_framework.response import Response
from api.serializers import InputPhotoSerializer

from os import PathLike
from typing import Union


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
            return Response('JSON structure is invalid', status=400)

        failures = []
        json_data = json_data[:5]  # Restricted to 10 for demonstration
        for j in json_data:
            serializer = InputPhotoSerializer(data=j)
            save = serializer.save_photo()

            # On fail saves JSON for details
            if save.status_code != 200:
                failures.append(j)

        return Response(cls._craft_response(json_data, failures), status=200)

    @staticmethod
    def _craft_response(json_data, failures):
        fails = len(failures)
        return {
            'successful': len(json_data) - fails,
            'failed': {
                'count': fails,
                'details': failures
            }
        }

    @classmethod
    def import_from_url(cls, url: str):
        if not url_is_valid(url):
            return Response('Provided URL is invalid', status=400)

        try:
            json_data = requests.get(url).json()
        except json.JSONDecodeError:
            return Response('Could not parse JSON from provided URL', status=400)

        return cls._import_json(json_data)

    @classmethod
    def import_from_local_file(cls, path: Union[str, bytes, PathLike]):
        try:
            with open(path) as f:
                json_data = json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            return Response('Filetype must be .json', status=400)
        except PermissionError:
            return Response('Permission denied. Passed directory instead of a file?', status=400)
        except FileNotFoundError:
            return Response('File not found', status=400)

        return cls._import_json(json_data)
