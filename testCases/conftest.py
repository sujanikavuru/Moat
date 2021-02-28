from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path='./drivers/geckodriver')
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# pytest html report
@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata['Project Name'] = "MOAT"
    config._metadata['Module Name'] = "Search Brand"
    config._metadata['Tester'] = "Sujani"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("plugins", None)
