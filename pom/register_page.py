from selenium.webdriver.common.by import By
from pom.base import BaseDriver

class RegisterPage(BaseDriver):
    """TODO 实现注册页面的封装"""
    _register_name = By.ID,'loginname'
    _register_pass = By.ID,'pass'
    _register_repass = By.ID, 're_pass'
    _register_email = By.ID,'email'
    _register_btn = By.CSS_SELECTOR, '[value="注册"]'


    _register_error_result = By.CSS_SELECTOR,'div[class="alert alert-error"]>strong'
    _register_success_result = By.CSS_SELECTOR, 'div[class="alert alert-success"]>strong'

    @property
    def regiseter_name(self):
        return self.driver.find_element(*self._register_name)

    @property
    def register_pass(self):
        return self.driver.find_element(*self._register_pass)

    @property
    def register_repass(self):
        return self.driver.find_element(*self._register_repass)

    @property
    def register_email(self):
        return self.driver.find_element(*self._register_email)

    @property
    def register_btn(self):
        return self.driver.find_element(*self._register_btn)

    @property
    def register_error_result(self):
        return self.driver.find_element(*self._register_error_result)

    @property
    def register_success_result(self):
        return self.driver.find_element(*self._register_success_result)