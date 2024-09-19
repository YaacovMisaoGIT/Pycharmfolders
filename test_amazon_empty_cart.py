from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAmazonCart:
    driver = ''

    def setup_method(self):
        service = Service(executable_path=r"C:/Users/Public/Automation-PyCharm-Mini/pythonProject/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.amazon.in")
        self.driver.set_window_size(1920, 1380)

    def test_amazon_empty_cart(self):
        self.driver.find_element(By.ID, 'nav-cart-count').click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-empty-cart']//h2").text
        expected_text = "Your Amazon Cart is empty"
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but actual text: {actual_text}'"




    def teardown_method(self):
        self.driver.quit()