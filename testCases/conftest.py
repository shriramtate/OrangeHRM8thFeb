import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching Headless Browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = None
        print("Invalid Browser")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()