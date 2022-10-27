from api.models import PhotoFields
from django.core.management.base import BaseCommand
from data_import.json_importer import JSONImporter
from data_import.webdriver import WebDriver


class Command(BaseCommand):
    help = 'Importing photos from third-party API'
    missing_args_message = 'No URL provided'

    def add_arguments(self, parser):
        parser.add_argument(PhotoFields.url, type=str, help='URL to import from')

    def handle(self, *args, **kwargs):
        url = kwargs[PhotoFields.url]
        result = JSONImporter.import_from_url(url)

        print(result.data)
        WebDriver.close()
