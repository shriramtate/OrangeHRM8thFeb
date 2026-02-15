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

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


#Test Data
@pytest.fixture(params = [
    ("Admin", "admin123", "login_pass"), # All correct #
    ("Admin1", "admin123", "login_fail"), # username wrong #
    ("Admin", "admin1234", "login_fail"), # password wrong
    ("Admin1", "admin1234", "login_fail")  # username and password wrong
])
def Orange_HRM_login_data(request):
    return request.param
