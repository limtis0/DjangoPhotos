import requests
from data_import.json_importer import JSONImporter


class TestJSONImporter:
    def test_is_json_valid(self):
        response = requests.get('https://jsonplaceholder.typicode.com/photos')
        assert JSONImporter._is_json_valid(response.json()) is True
