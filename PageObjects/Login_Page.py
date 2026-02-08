from selenium.webdriver.common.by import By


class login_page_class:
    textbox_username_XPATH="//input[@placeholder='Username']"
    textbox_password_XPATH="//input[@placeholder='Password']"
    login_button_XPATH="//button[@type='submit']"
    click_menu_XPATH="//span[@class='oxd-userdropdown-tab']"
    click_logout_XPATH="//a[normalize-space()='Logout']"



    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_XPATH).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_XPATH).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_XPATH).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_XPATH).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_XPATH).click()

    def click_menu(self):
        self.driver.find_element(By.XPATH, self.click_menu_XPATH).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.click_logout_XPATH).click()

    def verify_login(self):
        try:
            self.driver.find_element(By.XPATH, self.click_menu_XPATH)
            return "Login Successful"
        except:
            return "Login Failed"