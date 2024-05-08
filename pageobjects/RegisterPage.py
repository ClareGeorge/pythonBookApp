from typing import Tuple

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage:
    page_title = (By.XPATH, "//form//../h4[text()='Register to Book Store']")
    recaptcha_checkbox = (By.XPATH, "//*[@class='rc-anchor-center-container']//../*[@role='checkbox']")
    recaptcha_frame = (By.XPATH, "//iframe[@title='reCAPTCHA']")
    firstname_textbox = (By.ID, "firstname")
    lastname_textbox = (By.ID, "lastname")
    username_textbox = (By.ID, "userName")
    password_textbox = (By.ID, "password")
    register_button = (By.ID, "register")
    error_message = (By.XPATH, "//div[@id='output']//../*[contains(text(), 'Passwords must have at least one non alphanumeric')]")
    def __init__(self, driver):
        self.driver = driver
    def register_new_user(self,):
        message = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*RegisterPage.page_title).is_displayed())
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(RegisterPage.firstname_textbox))

        firstname_elem = self.driver.find_element(*RegisterPage.firstname_textbox)
        self.driver.execute_script("return arguments[0].scrollIntoView();", firstname_elem)
        firstname_elem.send_keys("Clare")

        lastname_elem = self.driver.find_element(*RegisterPage.lastname_textbox)
        self.driver.execute_script("return arguments[0].scrollIntoView();", lastname_elem)
        lastname_elem.send_keys("Clare")

        username_elem = self.driver.find_element(*RegisterPage.username_textbox)
        self.driver.execute_script("return arguments[0].scrollIntoView();", username_elem)
        username_elem.send_keys("Clare")

        password_elem = self.driver.find_element(*RegisterPage.password_textbox)
        self.driver.execute_script("return arguments[0].scrollIntoView();", password_elem)
        password_elem.send_keys("Clare")


        WebDriverWait(self.driver,10).until(expected_conditions.frame_to_be_available_and_switch_to_it(RegisterPage.recaptcha_frame))
        recaptcha_check_elem = self.driver.find_element(*RegisterPage.recaptcha_checkbox)
        self.driver.execute_script("return arguments[0].scrollIntoView();", recaptcha_check_elem)
        recaptcha_check_elem.click()

        self.driver.switch_to.default_content()

        register_button_elem = self.driver.find_element(*RegisterPage.register_button)
        self.driver.execute_script("return arguments[0].scrollIntoView();", register_button_elem)
        register_button_elem.click()

        assert WebDriverWait(self.driver, 10).until(lambda x : x.find_element(*RegisterPage.error_message).is_displayed) == True

        self.driver.execute_script("return arguments[0].scrollIntoView();", password_elem).send_keys("Clare1*Sydney")

        #Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer.

        WebDriverWait(self.driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(RegisterPage.recaptcha_frame))
        self.driver.execute_script("return arguments[0].scrollIntoView();", recaptcha_check_elem)
        recaptcha_check_elem.click()

        self.driver.switch_to.default_content()

        self.driver.execute_script("return arguments[0].scrollIntoView();", register_button_elem)
        register_button_elem.click()
        print("hello")