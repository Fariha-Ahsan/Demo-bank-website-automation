import time
import unittest
import pytest
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import xl_util
import openpyxl



class BankLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "https://www.demo.guru99.com/V4/"

    # invalid ID and valid Password
    def test_login(self):
        path = "C://Users/Raha/PycharmProjects/demoBankAutomation/testData.xlsx"
        rows = xl_util.rowCount(path, "Data")
        for i in range(2, rows):
            username = xl_util.readFile(path, "Data", i, 2)
            password = xl_util.readFile(path, "Data", i, 3)
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.driver.find_element(By.XPATH, "//input[@name='uid']").send_keys(username)
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
            self.driver.find_element(By.XPATH, "//input[@name='btnLogin']").click()
            time.sleep(3)
            try:
                alert = self.driver.switch_to.alert.text
                print(alert)
                self.driver.switch_to.alert.accept()
                time.sleep(5)
                exp_alert = "User or Password is not valid"
                if alert==exp_alert:
                    print("test case "+str(i)+" passed")
                else:
                    print("test case "+str(i)+" failed")
            except NoAlertPresentException:
                actual_title = self.driver.title
                if "Guru99 Bank Manager HomePage"==actual_title:
                    print("passed test case "+str(i))
                else:
                    print("failed test case "+str(i))
                time.sleep(2)



    def tearDown(self):
        self.driver.close()
