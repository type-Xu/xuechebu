"""
登录页面
"""
import page
from base.base_page import BasePage


class MinePage(BasePage):
    def click_login_btn(self):
        """点击登录按钮"""
        self.click_func(page.login)

