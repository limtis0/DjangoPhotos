import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WebDriver(metaclass=Singleton):
    initialized = False

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        # _options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = WebDriver.driver = webdriver.Chrome(service=service, options=options)
        self.__class__.initialized = True

    @classmethod
    def close(cls):
        if not cls.initialized:
            return

        # This is a hack
        # Selenium hangs while handling SIGINT (for a minute or so): https://github.com/SeleniumHQ/selenium/issues/9835
        for proc in psutil.process_iter():
            if proc.name() in ('chrome.exe', 'chromedriver.exe'):
                proc.kill()
