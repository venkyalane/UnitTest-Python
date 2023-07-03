from logfile import get_the_logs
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

log = get_the_logs()

class PythonOrgSearch(unittest.TestCase):
    log.info("UnitTest started")
    def setUp(self):
        self.driver = webdriver.Firefox()
        log.info("browser successfully opened")
        self.driver.implicitly_wait(115)

    def test_search_in_python_org(self):
        driver = self.driver
        log.info("URL entered")
        driver.get("http://www.python.org")
        log.info("web page successfully opened")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        log.info("pycon typed in search box")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        log.info("UnitTest pass")
        self.driver.close()
        log.info("browser successfully closed")

if __name__ == "__main__":
    unittest.main()
