from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class UserLogin():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://localhost:8080/taxexam/"
        self.username = 'admin'
        self.password = 'xxb!(@zsx'

    '''
    function：登陆主页面后点击已阅读按钮
    '''
    def clickReadedButton(self):
        self.driver.find_element_by_id("btnclose").click()

    def NormalLogin(self):
        driver = self.driver
        driver.find_element_by_name("j_username").send_keys(self.username)
        driver.find_element_by_name("j_password").send_keys(self.password)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/form/div[3]/div/button[1]").click()


    def adminLogin(self):
        driver = self.driver
        driver.get(self.base_url)
        self.clickReadedButton()
        time.sleep(2)
        driver.find_element_by_link_text("登录").click()
        time.sleep(2)
        driver.find_element_by_name("j_username").send_keys(self.username)
        driver.find_element_by_name("j_password").send_keys(self.password)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/form/div[3]/div/button[1]").click()
        time.sleep(3)
        print(driver.title)
        try:
            assert driver.title == '第五届“税收和注册税务师知识竞赛”——试卷管理'
            print("assert Pass!")
        except Exception as e:
            print("assert Failed!", format(e))

    def StartMatch(self):
        driver = self.driver
        driver.get(self.base_url)
        self.clickReadedButton()
        driver.find_element_by_link_text("开始竞赛").click()
        driver.find_element_by_link_text('第五届“税收和注册税务师知识竞赛”').click()
        time.sleep(2)
        self.NormalLogin()

    def addQuestions(self, content):
        self.adminLogin()
        driver = self.driver
        print('WebElement类方法：', driver.find_element_by_link_text("添加试题").get_property('text'))
        driver.find_element_by_link_text("添加试题").click()

        # 智能等待5S,失败后异常信息中带有message
        WebDriverWait(driver, 5, 1).until(method=lambda x: x.find_element_by_css_selector("#field-select > option"),\
                                          message="等待5S，页面未能进入添加试题页面...")
        driver.find_element_by_css_selector("#field-select > option").click()
        # 最大化窗口
        driver.maximize_window()
        driver.find_element_by_css_selector("#point-from-select > option").click()
        driver.find_element_by_css_selector("#add-point-btn").click()


    # 答题，比对选择的答案和从数据库提取的答案
    # SELECT answer FROM et_question WHERE name = '个体工商户下列支出准';





# #刷新当前页面
# refresh = browser.refresh()
# time.sleep(3)
# browser.quit()
