from selenium.webdriver.common.by import By

from pom.base import BaseDriver


class MainPage(BaseDriver):

    _login_link = By.LINK_TEXT,"登录"
    _register_link = By.LINK_TEXT,'注册'
    _user_login_name = By.CSS_SELECTOR,'span.user_name>a.dark'

    @property
    def register_link(self):
        """
        登录链接
        :return:
        """
        return self.driver.find_element(*self._register_link)

    @property
    def login_link(self):
        """
        登录链接
        :return:
        """
        return self.driver.find_element(*self._login_link)


    @property
    def user_name_link(self):
        return self.driver.find_element(*self._user_login_name)