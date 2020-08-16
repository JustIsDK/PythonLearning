"""
用户模块
"""
from pom.login_page import LoginPage
from pom.register_page import RegisterPage

class UserModel:
    def __init__(self):
        self.loginPage = LoginPage()
        self.registerPage = RegisterPage()

    def user_login(self,username,passwd):
        """
        使用用户名和密码进行登录
        :param username:
        :param passwd:
        :return:
        """
        self.loginPage.login_name.clear()
        self.loginPage.login_name.send_keys(username)
        self.loginPage.login_pass.clear()
        self.loginPage.login_pass.send_keys(passwd)
        self.loginPage.login_btn.click()

    def user_register(self,username,passwd,repasswd,emial):
        self.registerPage.regiseter_name.clear()
        self.registerPage.regiseter_name.send_keys(username)

        self.registerPage.register_pass.clear()
        self.registerPage.register_pass.send_keys(passwd)

        self.registerPage.register_repass.clear()
        self.registerPage.register_repass.send_keys(repasswd)

        self.registerPage.register_email.clear()
        self.registerPage.register_email.send_keys(emial)

        self.registerPage.register_btn.click()

    def get_register_result(self,is_sucees=False):
        if not is_sucees:
            return self.registerPage.register_error_result.text
        else:
            return self.registerPage.register_success_result.text
