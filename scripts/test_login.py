"""
测试用例
"""
import pytest

from common.utils import init_driver
from page.page_factory import PageFactory
from tool.read_file import build_login_data


class TestLogin(object):
    def setup(self):
        self.driver = init_driver()  # 驱动对象
        self.factory = PageFactory(self.driver)  # 工厂类对象

    def teardown(self):
        self.driver.quit()  # 退出

    @pytest.mark.parametrize('name,pwd', build_login_data())
    def test_login(self, name, pwd):
        self.factory.homepage().click_minepage()  # 点击我的
        self.factory.minepage().click_login_btn()  # 点击我的页面登录
        self.factory.loginpage().input_name(name)  # 账号
        self.factory.loginpage().input_pwd(pwd)  # 密码
        self.factory.loginpage().click_login_bar()  # 登录

      
