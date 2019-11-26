"""
po工厂
"""
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):
    def __init__(self, driver):
        self.driver = driver

    def homepage(self):
        """主页面"""
        return HomePage(self.driver)

    def minepage(self):
        """我的页面"""
        return MinePage(self.driver)

    def loginpage(self):
        """登录页面"""
        return LoginPage(self.driver)


