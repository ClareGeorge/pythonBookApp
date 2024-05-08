from time import sleep

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", default = "chrome" ,action = "store" , help= " 2 options : chorme or edge")


driver : webdriver
def set_ChromeBrowser() -> webdriver:

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certification-errors")

    service = webdriver.ChromeService()
    service.service_args = ["--log-level=DEBUG", "--append-log", "--readable-timestamp"]

    driver = webdriver.Chrome(service=service, options= options)
    return driver



def set_EdgeBrowser() -> webdriver:


    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certification-errors")

    service = webdriver.EdgeService()
    service.service_args = ["--log-level=DEBUG", "--append-log", "--readable-timestamp"]

    driver = webdriver.Chrome(service=service, options=options)
    return driver


@pytest.fixture(scope='class')
def setup(request, ):
    global driver
    browser_name =  request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = set_ChromeBrowser()
    elif browser_name == "edge":
        driver = set_EdgeBrowser()

    request.cls.driver = driver
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()



