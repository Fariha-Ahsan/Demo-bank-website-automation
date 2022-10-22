
from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

class NewCustomerPage(unittest.TestCase):
    def setUp(self):
        browser = self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        #browser.execute_script("window.scrollTo(2,document.body.scrollHeight)")


        self.base_url="https://www.demo.guru99.com/V4/manager/addcustomerpage.php"
    def test_customer_name_box(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        name_box=driver.find_element(By.XPATH,"//input[@name='name']")
        name_box.send_keys("Abdur Rahman")
        time.sleep(3)
    def test_gender_field(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        gender_field=driver.find_element(By.XPATH,"//input[@value='m']")
        gender_field.click()
    def test_address_field(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        address_field=driver.find_element(By.XPATH,"//textarea[@name='addr']")
        address_field.send_keys("Dhaka,Bangladesh")
        time.sleep(2)


    def test_input_birth_date(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        dates=driver.find_element(By.XPATH,"//input[@id='dob']")
        dates.send_keys("09252013")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()