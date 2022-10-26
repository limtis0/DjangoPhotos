import requests
from data_import.json_parser import JSONParser


class TestJSONParser:
    def test_is_json_valid(self):
        response = requests.get('https://jsonplaceholder.typicode.com/photos')
        assert JSONParser._is_json_valid(response.json()) is True
