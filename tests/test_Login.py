from pageobjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    pass

    def test_Login(self):
        log = BaseClass.getLogger()

        login_page = LoginPage(self.driver)
        title = login_page.navigate_to_login_page("https://demoqa.com/login")
        log.info("The page title is" + title)

        message = login_page.verify_login()
        if message == True:
            log.info("Login failed")
            register_page = login_page.navigate_to_new_user()
            register_page.register_new_user()
        else:
            log.info("Login passed")
