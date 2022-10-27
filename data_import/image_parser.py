from io import BytesIO
from PIL import Image
from base64 import b64decode
from api.models import PhotoFields

from .webdriver import WebDriver
from selenium.webdriver.remote.errorhandler import NoSuchElementException, InvalidArgumentException, WebDriverException


class ImageParser:
    @classmethod
    def get_image(cls, url: str):
        try:
            WebDriver().driver.get(url)

            # Create a canvas, set it's width and height equal to image's
            # Write image to canvas, translate to base64
            # Remove metadata prefix
            b64img = WebDriver().driver.execute_script(r'''
                var img = document.getElementsByTagName("img")[0];
                var canvas = document.createElement("canvas");
                canvas.width = img.width;
                canvas.height = img.height;
                var ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0);
                var dataURL = canvas.toDataURL("image/png");
                return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
            ''')

            # Decode from base64, translate to bytes and write to PIL image
            img = Image.open(BytesIO(b64decode(b64img)))
            return img

        except (NoSuchElementException, InvalidArgumentException, WebDriverException):
            return None

    # @classmethod
    # def get_image_legacy(cls, url: str):
    #     try:
    #         WebDriver().driver.get(url)
    #         # Takes a screenshot of a first img object found.
    #         screenshot = WebDriver().driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
    #         img = Image.open(BytesIO(screenshot))
    #         return img
    #     except (NoSuchElementException, InvalidArgumentException, WebDriverException):
    #         return None

    @staticmethod
    def _get_dominant_color(img: Image):
        img = img.resize((150, 150), resample=0)  # Minor optimization
        dominant_color = max(img.getcolors(maxcolors=22500), key=lambda x: x[0])  # Max count from List[(count, (RGB))]
        hex_value = '#%02x%02x%02x' % dominant_color[1][:3]  # Filter RGB tuple to HEX string
        return hex_value

    @classmethod
    def get_image_info(cls, img: Image):
        width, height = img.size
        dominant_color = cls._get_dominant_color(img)
        return {
            PhotoFields.width: width,
            PhotoFields.height: height,
            PhotoFields.dominant_color: dominant_color
        }
