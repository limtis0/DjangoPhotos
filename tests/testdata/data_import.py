from api.models import PhotoFields


class DataImport:
    valid_api = {PhotoFields.url: 'https://jsonplaceholder.typicode.com/photos'}
    invalid_api = {PhotoFields.url: 'https://google.com'}
    invalid_url = {PhotoFields.url: 'My name is Vladimir'}
    invalid_request = {'asdf': 'ghjk'}

    json_file_valid = 'tests/testdata/photos.json'
    json_file_invalid = 'tests/testdata/incorrect.json'
    test_dir = 'tests/testdata/'
    file_type_invalid = 'tests/testdata/data_photos.py'
    file_nonexistent = 'tests/testdata/IAmNonexistent12345.filetype'
