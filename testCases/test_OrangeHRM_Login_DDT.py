import pytest

from PageObjects.Login_Page import login_page_class
from utilities.XLutils import XLutils_class
from utilities.logger import logger_class
from utilities.readConfig import readConfig_class


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_DDT:

    login_url = readConfig_class.get_login_url()
    log = logger_class.get_logger()
    excel_file = ".\\TestData\\OrangeHRM_DDT.xlsx"
    sheet_name = "Sheet1"

    @pytest.mark.regression
    @pytest.mark.DDT
    def test_login_DDT_003(self, driver_setup):
        self.driver = driver_setup
        self.log.info("Navigating to OrangeHRM Login Page")
        self.log.info(f"Excel File: {self.excel_file}")
        self.log.info("Counting max Rows")
        row_count = XLutils_class.get_row_count(self.excel_file, self.sheet_name)
        result_list = []
        self.log.info("Entering For loop of checking each row credentials")
        for i in range(2, row_count + 1):
            username = XLutils_class.readXL_Data(self.excel_file, self.sheet_name, i, 2)
            password = XLutils_class.readXL_Data(self.excel_file, self.sheet_name, i, 3)
            expected_result = XLutils_class.readXL_Data(self.excel_file, self.sheet_name, i, 4)
            self.driver.get(self.login_url)
            login_page = login_page_class(self.driver)
            self.log.info(f"Entering Username: {username}")
            login_page.enter_username(username)
            self.log.info(f"Entering Password: {password}")
            login_page.enter_password(password)
            login_page.click_login()
            self.log.info("Clicking Login Button")

            if login_page.verify_login() == "Login Successful":
                self.log.info("Login Successful")
                login_page.click_menu()
                self.log.info("Clicking Menu Button")
                login_page.click_logout()
                self.log.info("Clicking Logout Button")
                actual_result = "Login Successful"
            else:
                self.log.info("Login Failed")
                actual_result = "Login Failed"
            XLutils_class.writeXL_Data(self.excel_file, self.sheet_name, i, 5, actual_result)

            if actual_result == expected_result:
                test_status = "Pass"
                result_list.append("Pass")
            else:
                test_status = "Fail"
                result_list.append("Fail")
            XLutils_class.writeXL_Data(self.excel_file, self.sheet_name, i, 6, test_status)

        self.log.info("Checking if any test case failed")
        assert "Fail" not in result_list
        self.log.info("All test cases passed")
        self.log.info("Test Case Completed")
        self.log.info("=============================================================")

