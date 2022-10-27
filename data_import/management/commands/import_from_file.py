from django.core.management.base import BaseCommand
from data_import.json_importer import JSONImporter
from data_import.webdriver import WebDriver


class Command(BaseCommand):
    help = 'Importing photos from JSON file'
    missing_args_message = 'No file provided'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='File to import from. '
                                                        'Must contain [*{title:str, albumId: int, url: str}]')

    def handle(self, *args, **kwargs):
        path = kwargs['file_path']
        result = JSONImporter.import_from_local_file(path)

        print(result.data)
        WebDriver.close()
