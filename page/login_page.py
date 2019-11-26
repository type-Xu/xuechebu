"""
注册-主页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    def input_name(self, text):
        """输入按钮"""
        self.input_func(page.name, text)

    def input_pwd(self, text):
        """输入按钮"""
        self.input_func(page.pwd, text)

    def click_login_bar(self):
        """点击登录按钮"""
        self.click_func(page.login_btn)

    def click_com_btn(self):
        """点击弹窗登录提示按钮"""
        self.click_func(page.com_btn)
