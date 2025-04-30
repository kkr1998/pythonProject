import time
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Punch:

    time_icon_click_xpath = "//div[@class='orangehrm-attendance-card-bar']//button[@type='button']"
    calender_dropdown_click_xpath = "//i[@class='oxd-icon bi-calendar oxd-date-input-icon']"
    month_click_xpath = "//div[@class='oxd-calendar-selector-month-selected']"
    oct_click_xpath = "//li[text()='October']"
    year_dropdown_click_xpath = "//div[@class='oxd-calendar-selector-year-selected']"
    selected_year_click_xpath = "//ul[@class='oxd-calendar-dropdown']//li[text()='2024']"
    date_click_xpath = "//div[text()='11']"
    time_icon2_xpath = "//i[@class='oxd-icon bi-clock oxd-time-input--clock']"
    time_hour_xpath = "//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text']"
    time_minute_xpath = "//input[@class='oxd-input oxd-input--active oxd-time-minute-input-text']"
    punch_in_xpath = "//button[@type='submit']"



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def starting_time_click(self):

        try:
            element = self.driver.find_element(By.XPATH, self.time_icon_click_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print("Initial click failed:")
            traceback.print_exc()
            return

        xpaths = [
            self.calender_dropdown_click_xpath,
            self.month_click_xpath,
            self.oct_click_xpath,
            self.year_dropdown_click_xpath,
            self.selected_year_click_xpath,
            self.date_click_xpath
        ]

        for xpath in xpaths:
            try:
                time.sleep(2)
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))


                print("Element text:", element.text)

                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.driver.execute_script("arguments[0].click();", element)

            except Exception as e:
                print(f"Retrying due to error while clicking {xpath}:")
                traceback.print_exc()
                break


    def time_icon_time(self):
        element = self.driver.find_element(By.XPATH, self.time_icon2_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def hour_time(self, hours):
        self.driver.find_element(By.XPATH, self.time_hour_xpath).send_keys(hours)

    def minute_time(self, minute):
        self.driver.find_element(By.XPATH, self.time_minute_xpath).send_keys(minute)

    def punch_in(self):
        self.driver.find_element(By.XPATH, self.punch_in_xpath).click()





