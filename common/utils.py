from appium import webdriver


# com.bjcsxq.chat.carfriend/.MainActivity

def init_driver():
    """驱动获取方法"""
    capabilities = {
        "platformName": "Android",  # 平台类型
        "platformVersion": "5.1",  # 系统版本
        "deviceName": "模拟器",  # 设备名称
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测引用的包名
        "appActivity": ".MainActivity"  # 待测应用的启动名
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    # driver.implicitly_wait(10)  # 隐式等待
    return driver


if __name__ == '__main__':
    init_driver()
