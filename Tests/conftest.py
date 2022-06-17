import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


@pytest.fixture(params=["chrome"], scope='class')  # use ["chrome", "firefox"] for firefox in parallel
def init_driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        # prefs = {"download.default_directory": "C:\\Users\\User QA\\PycharmProjects\\NumberProvisioning\\errors"}
        # prefs = {"download.default_directory": "/Users/vanamali/PycharmProjects/Array_Assessment/errors"}  # macos
        # options.add_experimental_option("prefs", prefs)
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        """options = webdriver.ChromeOptions()
        options.headless = True
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)"""
        # web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif request.param == "firefox":
        """options = webdriver.FirefoxOptions()
        options.headless = True
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)"""
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    elif request.param == "safari":
        web_driver = webdriver.Safari()

    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    request.cls.driver = web_driver

    yield
    time.sleep(3)
    web_driver.close()
