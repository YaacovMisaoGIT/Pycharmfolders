import pytest
from selenium import webdriver
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import pytest

class TestLinkedln:

    def setup_method(self):
        service = Service(executable_path=r"C:/Users/Public/Automation-PyCharm-Mini/pythonProject/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
        time.sleep(1)

    @pytest.mark.repeat(10)
    def test_amazon_search_kites(self):
        search = self.driver.find_element(By.ID, 'username').send_keys("yaacovmisao@gmail.com");
        # time.sleep(2)
        search = self.driver.find_element(By.ID, 'password').send_keys("kanggui*007");
        # time.sleep(3)
        search = self.driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']").click();
        time.sleep(1)
        search = self.driver.find_element(By.XPATH, "//div[@class='artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view mn-connection-card__dropdown']//button[@class='artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view mn-connection-card__dropdown-trigger artdeco-button--tertiary artdeco-button--muted artdeco-button--circle p1']").click();
        time.sleep(1)
        # search = self.driver.find_element(By.XPATH, " //div[@class='artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view']//div[@aria-hidden='false']").click();

        dialog_box = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-hidden='false']"))
        )
        dialog_box.click()
        time.sleep(0)
        search = self.driver.find_element(By.XPATH, "//span[@class='artdeco-button__text']")
        time.sleep(1)



        # search = self.driver.find_element(By.XPATH, "//div[@class='artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view mn-connection-card__dropdown']//div[contains(@class, 'artdeco-dropdown__content')]").click();


        # dropdown = WebDriverWait(self.driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 "//div[@class='artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view mn-connection-card__dropdown']//div[@class='artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view']"))
        # )
        # dropdown.click()
        #
        #
        # time.sleep(3)








    def teardown_method(self):
        self.driver.quit();

# while True:
#     pass




