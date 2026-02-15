import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Login_Page import login_page_class
from utilities.logger import logger_class
from utilities.readConfig import readConfig_class

@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_Params():

    driver = None
    log = logger_class.get_logger()
    login_url = readConfig_class.get_login_url()

    @pytest.mark.regression
    @pytest.mark.params
    def test_login_params_004(self, Orange_HRM_login_data):
        username = Orange_HRM_login_data[0]
        password = Orange_HRM_login_data[1]
        expected_result = Orange_HRM_login_data[2]
        self.driver.get(self.login_url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.title_contains("OrangeHRM")) #OR
        # wait.until(expected_conditions.title_is("OrangeHRM")) #This will wait for the title to be "OrangeHRM"
        if self.driver.title == "OrangeHRM":
            print("you are landed on correct page ")
            self.log.info("OrangeHRM Login Page Title Verified")
        else:
            print("you are landed on wrong page ")
            self.log.info("OrangeHRM Login Page Title Verification Failed")

        login_page = login_page_class(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        self.log.info("Clicking Login Button")

        if login_page.verify_login() == "login_pass":
            self.log.info("Login Successful")
            self.driver.save_screenshot(".\\screenshots\\orangeHRM_login_params_004_pass.png")
            self.log.info("Screenshot saved successfully")
            allure.attach.file("screenshots\\orangeHRM_login_002_pass.png", name="Login Successful",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info("Clicking Menu")
            login_page.click_menu()
            self.log.info("Clicking Logout")
            login_page.click_logout()
            actual_result = "login_pass"
            self.log.info("Login Verification Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\orangeHRM_login_params_004_fail.png")
            self.log.info("Login Failed")
            allure.attach.file("screenshots\\orangeHRM_login_002_fail.png", name="Login Failed",
                               attachment_type=allure.attachment_type.PNG)
            actual_result = "login_fail"
            self.log.info("Login Verification Failed")

        if expected_result==actual_result:
            self.log.info("Login Verification Passed")
            allure.attach.file("screenshots\\orangeHRM_login_params_004_pass.png", name="Login Verification Passed",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info("Test Case Passed")
            assert True
        else:
            self.log.info("Login Verification Failed")
            allure.attach.file("screenshots\\orangeHRM_login_params_004_fail.png", name="Login Verification Failed",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info("Test Case Failed")
            assert False
        self.log.info("Login Test Completed")
        self.log.info("=============================================================")
