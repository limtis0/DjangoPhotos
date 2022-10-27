from django.core.management.base import BaseCommand
from data_import.json_importer import JSONImporter
from data_import.webdriver import WebDriver


class Command(BaseCommand):
    help = 'Importing photos from third-party API'
    missing_args_message = 'No URL provided'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL to import from. '
                                                  'Must contain {title:str} {albumId: int}, {url: str}')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        result = JSONImporter.import_from_url(url)

        print(result.data)
        WebDriver.close()
