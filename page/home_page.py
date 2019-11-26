"""
我的页面
"""
import page
from base.base_page import BasePage


class HomePage(BasePage):
    def click_minepage(self):
        """点击我的按钮"""
        self.click_func(page.mine)
