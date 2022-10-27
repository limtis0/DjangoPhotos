import requests

from api.urls import URL
from api.models import Photo, PhotoFields

from testdata.data_import import DataImport
from data_import.json_importer import JSONImporter


class TestImport:
    def test_is_json_valid(self):
        response = requests.get(DataImport.valid_api[PhotoFields.url])
        assert JSONImporter._json_is_valid(response.json()) is True

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

    def test_local_file_import(self, photo_cleanup):
        valid = JSONImporter.import_from_local_file(DataImport.json_file_valid)
        assert valid.status_code == 200, 'Import from local file not working'

        assert all(list(i.status_code == 400 for i in [
            JSONImporter.import_from_local_file(DataImport.json_file_invalid),
            JSONImporter.import_from_local_file(DataImport.test_dir),
            JSONImporter.import_from_local_file(DataImport.file_type_invalid),
            JSONImporter.import_from_local_file(DataImport.file_nonexistent)
        ])), 'Edge cases are handled incorrectly'

    def test_api_file_import(self, api_client, photo_cleanup):
        url = f'{URL.API_DIR}{URL.IMPORT_FILE}'

        with open(DataImport.json_file_valid) as f:
            import_valid = api_client.post(url, data={PhotoFields.file: f})
        assert import_valid.status_code == 200, 'Import from file by API is not working correctly'

        with open(DataImport.json_file_invalid) as f:
            import_invalid = api_client.post(url, data={PhotoFields.file: f})
        assert import_invalid.status_code == 400, 'Invalid import from file by API is handled incorrectly'
