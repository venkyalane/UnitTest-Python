#Login to facebook functionality test using unittest.
import time
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_the_logs():
    logger = logging.getLogger()
    filehandler = logging.FileHandler("facebooklogin.log")  # mode="w"
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)  # WARNING DEBUGE
    return logger

log = get_the_logs()

class Logintest(unittest.TestCase):

    def setUp(self):
        log.info("testcase started")
        self.driver = webdriver.Firefox()
        log.info("Web browser successfuly opened")
        self.driver.implicitly_wait(30)

    def test_login_function(self):
        log.info("url entered")
        self.driver.get("https://www.facebook.com/login/")
        self.driver.find_element(By.XPATH, "//input[@id='email']").clear()
        log.info("username entered")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("username")
        log.info("password entered")
        self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("password")
        log.info("clicked on login button")
        self.driver.find_element(By.XPATH, "//button[@id='loginbutton']").click()
        time.sleep(10)

    def tearDown(self):
        log.info("browser succcessfuly closed")
        self.driver.close()
        log.info("UnitTest pass")
if __name__ == "__main__":
    unittest.main()

