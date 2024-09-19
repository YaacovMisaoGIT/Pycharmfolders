import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAmazon:
    driver = ''

    def setup_method(self):
        service = Service(executable_path=r"C:/Users/Public/Automation-PyCharm-Mini/pythonProject/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.amazon.in")
        # time.sleep(4)

    def test_amazon_bestsellers(self):
        self.driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[contains(@href,'bestsellers')]").click()
        actual_links = self.driver.find_elements(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-mobile-tabs__1W5ZT']//li")
        assert len(actual_links) == 0, f'Expected to see 5 bestsellers, but got {len(actual_links)}'



    def teardown_method(self):
        self.driver.quit()


# while True:
#     pass




