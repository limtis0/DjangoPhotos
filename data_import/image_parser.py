from io import BytesIO
from PIL import Image

from .webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.errorhandler import NoSuchElementException

from .url_is_valid import url_is_valid


class ImageParser:
    @classmethod
    def get_image(cls, url: str):
        if not url_is_valid(url):
            return False

        WebDriver().driver.get(url)
        try:
            # Takes a partial screenshot of a first img object found
            screenshot = WebDriver().driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
            img = Image.open(BytesIO(screenshot))
            return img
        except NoSuchElementException:
            return False
