import time

from page.login import Login
from utilities.readproperties import Readconfig
from page.punchTime import Punch
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert






class TestOrange:
    base_url = Readconfig.getbase_url()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    hours = Readconfig.getusername()
    mnt = Readconfig.getpassword()

    def test_dashboard(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        self.pg = Login(self.driver)
        self.pg.username(self.username)
        self.pg.password(self.password)
        self.pg.login_click()
        title = self.driver.title
        assert title == 'OrangeHRM'
        pass
        print(f"page title: {title}")

        # WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # alert = self.driver.switch_to.alert
        # alert.accept()
        # time.sleep(5)


    def test_punch_time(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        self.pt = Punch(self.driver)
        self.pt.starting_time_click()
        self.pt.time_icon_time()
        self.pt.hour_time(self.hours)
        self.pt.minute_time(self.mnt)
        self.pt.punch_in()

