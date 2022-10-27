import os
import sys
import signal
from .webdriver import WebDriver


def gracefully_shutdown(*_):
    # Prevents running code twice
    if os.environ.get('RUN_MAIN'):
        WebDriver.close()

    sys.exit(0)


signal.signal(signal.SIGINT, gracefully_shutdown)
signal.signal(signal.SIGTERM, gracefully_shutdown)
