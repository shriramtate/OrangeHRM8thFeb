import allure
import pytest

from PageObjects.Login_Page import login_page_class
from utilities.logger import logger_class
from utilities.readConfig import readConfig_class


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login:
    driver = None
    username = readConfig_class.get_username()
    password = readConfig_class.get_password()
    login_url = readConfig_class.get_login_url()
    log = logger_class.get_logger()
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Verify OrangeHRM Login Page")
    @allure.description("This test verifies the OrangeHRM login page by checking its title.")
    @allure.step("Verify OrangeHRM Login Page")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/OrangeHRM/OrangeHRM/issues/1234", name="OrangeHRM Login Page Issue")
    @allure.testcase("https://github.com/OrangeHRM/OrangeHRM/issues/5678", name="OrangeHRM Login Page Testcase")
    @allure.feature("OrangeHRM Login")
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_verify_url(self):
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page loaded successfully")
        if self.driver.title == "OrangeHRM":
            self.log.info("OrangeHRM Login Page Title Verified")
            self.driver.save_screenshot("screenshots\\orangeHRM_login_001.png")
            self.log.info("Screenshot saved successfully")
            allure.attach.file("screenshots\\orangeHRM_login_001.png", name="test_verify_url_pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.driver.save_screenshot("screenshots\\orangeHRM_login_001_fail.png")
            self.log.info("OrangeHRM Login Page Title Verification Failed")
            allure.attach.file("screenshots\\orangeHRM_login_001_fail.png", name="OrangeHRM Login Page Failure", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Test Completed")
        self.log.info("=============================================================")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Verify OrangeHRM Login")
    @allure.description("This test verifies the OrangeHRM login functionality.")
    @allure.step("Verify OrangeHRM Login")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/OrangeHRM/OrangeHRM/issues/1234", name="OrangeHRM Login Issue")
    @allure.testcase("https://github.com/OrangeHRM/OrangeHRM/issues/5678", name="OrangeHRM Login Testcase")
    @allure.feature("OrangeHRM Login")
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_verify_login_002(self):
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page loaded successfully")
        login_page = login_page_class(self.driver)
        self.log.info("Entering Username")
        login_page.enter_username(self.username)
        self.log.info("Entering Password")
        login_page.enter_password(self.password)
        login_page.click_login()
        self.log.info("Clicking Login Button")
        if login_page.verify_login() == "Login Successful":
            self.log.info("Login Successful")
            self.driver.save_screenshot("screenshots\\orangeHRM_login_002_pass.png")
            self.log.info("Screenshot saved successfully")
            allure.attach.file("screenshots\\orangeHRM_login_002_pass.png", name="Login Successful", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.driver.save_screenshot("screenshots\\orangeHRM_login_002_fail.png")
            self.log.info("Login Failed")
            allure.attach.file("screenshots\\orangeHRM_login_002_fail.png", name="Login Failed", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("Login Test Completed")
        self.log.info("=============================================================")





#pytest -v -s --browser chrome testCases/test_orangeHRM_login_001.py --html=Reports/orangeHRM_login_001.html

#pytest -v -s --browser chrome --html=Reports/orangeHRM_login_001.html --alluredir=Allure_Reports
#pytest -v --browser edge --html=Reports/orangeHRM_login_002.html --alluredir=Allure_Reports