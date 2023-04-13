import time

import allure
from selenium.webdriver.common.by import By

import mes
from selenium import webdriver

class TestCeshien:
    #前置 所有用例执行之前执行一次
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
    #每个用例执行前会执行一次
    def setup(self):
        self.driver.get(mes.MesID.url)
        self.driver.maximize_window()
    #所有用例执行后执行一次
    def teadown_class(self):
        self.driver.quit()

    #正向测试用例
    def test_search(self):
        """
        搜索selenium内容
        测试步骤
        1、打开测试网站
        2、点击搜索按钮
        3、点击高级搜索按钮
        4、输入selenium搜索内容
        5、选择类别标签
        6、点击搜索
        7、断言信息是否正确
        """
        # 点击搜索按钮
        self.driver.find_element(By.ID, mes.MesID.search_button).click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CLASS_NAME, mes.MesID.advanced_search_class).click()
        # 输入搜索内容selenium
        self.driver.find_element(By.XPATH, mes.MesID.search_input).send_keys("selenium")
        # 点击搜索类别下拉框
        self.driver.find_element(By.ID, "search-type").click()
        # 点击第二个选项
        self.driver.find_element(By.XPATH, """//*[@class="select-kit-collection"]/li[2]""").click()
        # 点击搜索按钮
        self.driver.find_element(By.XPATH, mes.MesID.button).click()
        # 获取搜索结果的类别
        res_head = self.driver.find_element(By.CLASS_NAME, "tag-heading")
        # 获取搜索结果的内容
        res_item = self.driver.find_element(By.CLASS_NAME, "tag-items")
        # 断言类别与内容是否正确
        assert "标签" == res_head.text
        assert "selenium" == res_item.text

    # 搜索内容为空测试用例
    def test_searchnull(self):
        """
        搜索内容为空时
        测试步骤
        1、打开测试网站
        2、点击搜索按钮
        3、点击高级搜索按钮
        4、不输入内容，点击搜索按钮
        7、断言信息是否正确
        """
        # 点击搜索按钮
        self.driver.find_element(By.ID, mes.MesID.search_button).click()
        # 点击高级搜索按钮
        self.driver.find_element(By.CLASS_NAME, mes.MesID.advanced_search_class).click()
        # 点击搜索按钮
        self.driver.find_element(By.XPATH, mes.MesID.button).click()
        # 获取搜索结果
        res = self.driver.find_element(By.CLASS_NAME, "search-notice")
        # 截图操作
        self.driver.save_screenshot("search_null.png")
        # 塞入报告(ps：执行时要用命令行的方式执行，命令：pytest test_ceshiern.py(用例文件名) --alluredir=./report(指定报告路径)
        # 查看报告 allure serve 报告名称report
        allure.attach.file("search_null.png", name="搜索内容为空", attachment_type=allure.attachment_type.PNG)
        # 断言类别与内容是否正确
        assert "您的搜索词过短。" == res.text

