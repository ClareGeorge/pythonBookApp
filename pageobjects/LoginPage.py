from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.RegisterPage import RegisterPage


class LoginPage:
    welcome_str = (By.XPATH, "//h2[text()='Welcome,']")
    username_texbox = (By.XPATH, "//input[@id='userName']")
    password_textbox = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[id='login']")
    error_message = (By.XPATH, "//div[@id='output']/div/p[@id='name']")
    newuser_button = (By.CSS_SELECTOR, "button[id='newUser']")

    def __init__(self, driver:webdriver):
        self.driver = driver
        print("adding drivers")

    def navigate_to_login_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10) .until(lambda x: x.find_element(*LoginPage.welcome_str).is_displayed())
        return self.driver.title

    def verify_login(self,):
        self.driver.find_element(*LoginPage.username_texbox).send_keys("ctest123")
        self.driver.find_element(*LoginPage.password_textbox).send_keys("ctest123")

        login_button_elem = self.driver.find_element(*LoginPage.login_button)
        self.driver.execute_script("return arguments[0].scrollIntoView();", login_button_elem)
        login_button_elem.click()

        message = WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(LoginPage.error_message, text_= "Invalid username or password!"))
        return  message
    def navigate_to_new_user(self):

        newuser_button_elem = self.driver.find_element(*LoginPage.newuser_button)
        self.driver.execute_script("return arguments[0].scrollIntoView();", newuser_button_elem)
        newuser_button_elem.click()
        return RegisterPage(self.driver)




