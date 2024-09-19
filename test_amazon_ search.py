import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

class TestAmazon:
    search_words = ('dress', 'shoes', 'books')
    driver = ''

    def setup_method(self):
        service = Service(executable_path=r"C:/Users/Public/Automation-PyCharm-Mini/pythonProject/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.amazon.in")
        self.driver.set_window_size(1920, 1380)

    @pytest.mark.parametrize("search_query", search_words)
    def test_amazon_search(self, search_query):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)
        time.sleep(5)

    def test_amazon_search_kites(self):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys("kites", Keys.ENTER)
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()

# while True:
#     pass




