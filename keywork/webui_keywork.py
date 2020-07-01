from selenium import webdriver
from selenium.webdriver.common.by import By
from options.chrome_options import Options
from time import sleep
from log.log import Logger
# #v1.0
# def open_browser(browser_type):
#     browser_type = browser_type.upper()
#     if browser_type is 'CHR':
#         driver = webdriver.Chrome()
#     elif browser_type is 'IE':
#         driver = webdriver.Ie()
#     elif browser_type is 'FF':
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Chrome()
#     return driver

#v2.0
def open_browser(browser_type):
    try:
        if browser_type == 'CHR':
            Logger().log().info('正常启动浏览器中......')
            driver = webdriver.Chrome(options=Options().options_conf())
        else:
            driver = getattr(webdriver, browser_type)()
    except Exception as e:
        Logger().log().info("输入浏览器类型错误，默认调用谷歌浏览器，错误信息{}".format(e))
        driver = webdriver.Chrome()

    return driver

class WebUIKeys:


    def __init__(self,browser_type):
        self.driver=open_browser(browser_type)


    def locator(self,loc_type,value):
        # v1.0
        # if loc_type is 'xpath':
        #     return self.driver.find_element_by_xpath(value)
        # elif loc_type is 'id':
        #     return self.driver.find_element_by_id(value)
        try:
            return self.driver.find_element(getattr(By,loc_type.upper()),value)
        except Exception as e:
            Logger().log().info("定位元素出现异常，异常信息：\n{}".format(e))

    def input(self,loc_type,value,txt):
        self.locator(loc_type,value).send_keys(txt)

    def click(self,loc_type,value):
        self.locator(loc_type,value).click()

    def quit(self):
        self.driver.quit()

    def visit(self,url):
        self.driver.get(url)


    def sleep(self,time):
        sleep(time)

    def wait(self,time):
        self.driver.implicitly_wait(time)

    def assert_text(self,loc_type,value,expect):
        reality = self.locator(loc_type,value).text
        try:
            assert reality == expect
            Logger().log().info("流程正确，断言成功！")
            return True
        except Exception as e:
            Logger().log().info("流程正确，断言失败！失败信息：{}".format(e))
            return False

