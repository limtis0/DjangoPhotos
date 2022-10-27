import json
import requests

import jsonschema
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

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
    def _json_is_valid(cls, json_data):
        try:
            jsonschema.validate(instance=json_data, schema=cls.schema)
            return True
        except jsonschema.ValidationError:
            return False

    @staticmethod
    def _url_is_valid(url: str):
        try:
            URLValidator()(url)
            return True
        except ValidationError:
            return False

    @classmethod
    def _import_json(cls, json_data):
        if not cls._json_is_valid(json_data):
            return Response('JSON structure is invalid', status=400)

        failures = []
        json_data = json_data[:20]  # Restricted to 20 for demonstration

        for data in json_data:
            serializer = InputPhotoSerializer(data=data)
            save = serializer.save_photo()

            # On fail saves JSON for details
            if save.status_code != 200:
                failures.append(data)

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
        if not cls._url_is_valid(url):
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
                return cls.import_from_file(f)
        except PermissionError:
            return Response('Permission denied. Passed directory instead of a file?', status=400)
        except FileNotFoundError:
            return Response('File not found', status=400)

    @classmethod
    def import_from_file(cls, file):
        try:
            json_data = json.load(file)
        except (UnicodeDecodeError, json.JSONDecodeError):
            return Response('Filetype must be .json', status=400)

        return cls._import_json(json_data)
