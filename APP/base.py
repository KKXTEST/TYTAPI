#coding:utf-8
import os
import time
from appium import webdriver
import unittest
desired_caps = {
            'platformName': 'Android' ,
            'deviceName': 'c20b2471',
            'platformVsrsion': '10.0',
            'appPackage': 'com.tyt.chezhu',
            'appActivity': '.activity.LoadingAct',
            'noReset': True,
            'unitcodeKryboard': True,
            'resetKeyboard':True,
            'newCommandTimeout': '1500000',
            'automationName': 'Uiautomator2'
        }
        #启动APP
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot("./SecPIC/start.PNG")
        time.sleep(2)
        #进入登录页面
        self.driver.find_elements_by_id()
    @classmethod
    def tearDwonClass(self):
        print('测试完成清理环境')
        self.driver.quit()

if __name__=='__main__':
    unittest.run()