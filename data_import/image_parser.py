from io import BytesIO
from PIL import Image, UnidentifiedImageError

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import NoSuchElementException
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
    def _get_image_requests(url: str):
        try:
            r = requests.get(url)
            img = Image.open(BytesIO(r.content))
            return img
        except (ValueError, UnidentifiedImageError):  # Blocked by CloudFlare or URL is incorrect
            return False

    @staticmethod
    def _get_image_selenium(url: str):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        try:
            # Takes a partial screenshot of a first img object found
            screenshot = driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
            img = Image.open(BytesIO(screenshot))
            return img
        except NoSuchElementException:
            return False
