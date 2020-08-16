from pom.main_page import MainPage
from bussiness.user_model import UserModel

class MainModel:

    def __init__(self):
        self.mainPage = MainPage()
        self.userModel = UserModel()

    def go_to_login_page(self):
        """
        跳转到登陆页面
        :return:
        """
        self.mainPage.login_link.click()
        return self.userModel

    def go_to_register_page(self):
        self.mainPage.register_link.click()
        return self.userModel

    @property
    def user_name_text(self):
        """
        获取用户文本值
        :return:
        """
        return self.mainPage.user_name_link.text
