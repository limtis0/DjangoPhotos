from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    driver = None

    @classmethod
    def close(cls):
        if cls.driver is not None:
            cls.driver.quit()


# Acts like a Singleton, loaded on import
_options = Options()
# _options.headless = True
_options.add_experimental_option('excludeSwitches', ['enable-logging'])
_service = Service(ChromeDriverManager().install())
WebDriver.driver = webdriver.Chrome(service=_service, options=_options)
