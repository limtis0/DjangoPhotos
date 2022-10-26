from io import BytesIO
from PIL import Image

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.errorhandler import NoSuchElementException

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ImageParser:
    @staticmethod
    def _is_url_valid(url: str):
        try:
            URLValidator()(url)
            return True
        except ValidationError:
            return False

    @staticmethod
    def get_webdriver():
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @classmethod
    def get_image(cls, driver: WebDriver, url: str):
        if not cls._is_url_valid(url):
            return False

        driver.get(url)
        try:
            # Takes a partial screenshot of a first img object found
            screenshot = driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
            img = Image.open(BytesIO(screenshot))
            return img
        except NoSuchElementException:
            return False
