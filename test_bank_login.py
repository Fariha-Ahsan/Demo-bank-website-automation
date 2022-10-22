import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import util

class BankLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver=self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url="https://www.demo.guru99.com/V4/"

    #invalid ID and valid Password
    def test_invalid_uid_login(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        user_id=self.driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("invalid ID")
        password=self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("edYgEpy")
        self.driver.find_element(By.XPATH,"//input[@name='btnLogin']").click()
        time.sleep(8)


        expected_alert="User or Password is not valid"
        alert=self.driver.switch_to.alert
        actual_alert =self.driver.switch_to.alert.text
        print(actual_alert)
        alert.accept()
        time.sleep(8)
        self.assertEqual(expected_alert,actual_alert)

    #invalid password and valid ID
    def test_invalid_pass(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr449307")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("password")
        driver.find_element(By.XPATH, "//input[@name='btnLogin']").click()
        time.sleep(4)
        alert=driver.switch_to.alert.text
        print(alert)
        driver.switch_to.alert.accept()
        time.sleep(5)
        exp_alert="User or Password is not valid"
        self.assertEqual(alert,exp_alert)

    #invalid password and ID
    def test_invalid_pass_ID(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("invalid ID")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("password")
        driver.find_element(By.XPATH, "//input[@name='btnLogin']").click()
        time.sleep(4)
        alert=driver.switch_to.alert.text
        print(alert)
        driver.switch_to.alert.accept()
        time.sleep(5)
        exp_alert="User or Password is not valid"
        self.assertEqual(alert,exp_alert)

    #valid ID and Password
    def test_login_valid_uid_pass(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        user_id=self.driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr449307")
        password=self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("edYgEpy")
        self.driver.find_element(By.XPATH,"//input[@name='btnLogin']").click()
        actual_title=self.driver.title
        self.assertEqual("Guru99 Bank Manager HomePage",actual_title)
        time.sleep(2)
    def test_click_new_customer(self):
        driver=self.driver
        driver.get("https://www.demo.guru99.com/V4/manager/Managerhomepage.php")
        driver.find_element(By.XPATH,"//a[normalize-space()='New Customer']").click()
    def tearDown(self):
        self.driver.close()
