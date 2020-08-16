from selenium.webdriver.common.by import By
from pom.base import BaseDriver


class LoginPage(BaseDriver):

    _login_name = By.ID,'name'
    _login_pass = By.ID,'pass'
    _login_btn = By.CSS_SELECTOR,'[type="submit"]'

    @property
    def login_name(self):
        """
        登录用户名输入框
        :return:
        """
        return self.driver.find_element(*self._login_name)

    @property
    def login_pass(self):
        """
        登录的密码输入框
        :return:
        """
        return self.driver.find_element(*self._login_pass)

    @property
    def login_btn(self):
        """
        登录按钮
        :return:
        """
        return self.driver.find_element(*self._login_btn)