import time

from selenium.webdriver.common import by

import public_mes
from selenium import webdriver


class Test_lagou():

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_lagou_search(self):
        self.driver.get(public_mes.Message.get_url)
        self.driver.maximize_window()
        if self.driver.find_element(by.By.ID, "cboxClose"):
            self.driver.find_element(by.By.ID, "cboxClose").click()
        time.sleep(2)
        search_txt = self.driver.find_element(by.By.ID, "search_input").send_keys("字节跳动")
        search_button = self.driver.find_element(by.By.ID, "search_button").click()
        mes = self.driver.find_element(by.By.XPATH, '''//div[@class="cl-right-top__1cCMk"]/h3/a''')
        assert "字节跳动" == mes.text
        