import pytest
import requests

from api.urls import URL
from api.models import Photo

from testdata.data_import import DataImport
from data_import.json_importer import JSONImporter


class TestImport:
    def test_is_json_valid(self):
        response = requests.get(DataImport.valid_api['url'])
        assert JSONImporter._is_json_valid(response.json()) is True

    @pytest.mark.django_db
    def test_url_import(self, api_client, photo_cleanup):
        url = f'{URL.API_DIR}{URL.IMPORT_API}'

        # Valid response
        import_valid = api_client.post(url, data=DataImport.valid_api)
        assert import_valid.status_code == 200, 'Could not import from API'
        assert len(Photo.objects.all()) > 1, 'Could not import from API'

        # Invalid response
        import_invalid_api = api_client.post(url, data=DataImport.invalid_api)
        assert import_invalid_api.status_code == 400, 'Invalid response is handled incorrectly'

        # Invalid url
        import_invalid_url = api_client.post(url, data=DataImport.invalid_url)
        assert import_invalid_url.status_code == 400, 'Invalid URL is handled incorrectly'

        # Invalid request
        import_invalid_request = api_client.post(url, data=DataImport.invalid_request)
        assert import_invalid_request.status_code == 400, 'Invalid request is handled incorrectly'
