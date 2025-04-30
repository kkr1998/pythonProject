

from selenium.webdriver.common.by import By



class Login:

    user_name_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    login_click_xpath = "//button[@type='submit']"



    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.XPATH, self.user_name_xpath).send_keys(username)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def login_click(self):
        self.driver.find_element(By.XPATH, self.login_click_xpath).click()





