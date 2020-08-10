from selenium import webdriver
from selenium.webdriver.common.by import By
from options.chrome_options import Options
from time import sleep
from log.log import Logger
import openpyxl
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

def load_workbook(workbook_path):
    return openpyxl.load_workbook(workbook_path)


class WebUIKeys:


    def __init__(self,browser_type):
        self.driver=open_browser(browser_type)


    def locator(self,**kwargs):
        # v1.0
        # if loc_type is 'xpath':
        #     return self.driver.find_element_by_xpath(value)
        # elif loc_type is 'id':
        #     return self.driver.find_element_by_id(value)
        try:
            return self.driver.find_element(getattr(By,kwargs['type'].upper()),kwargs['value'])
        except Exception as e:
            Logger().log().info("定位元素出现异常，异常信息：\n{}".format(e))

    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs["text"])

    def click(self,**kwargs):
        self.locator(**kwargs).click()

    def quit(self):
        self.driver.quit()

    def visit(self,**kwargs):
        self.driver.get(kwargs["text"])


    def sleep(self,**kwargs):
        sleep(kwargs["text"])

    def wait(self,**kwargs):
        self.driver.implicitly_wait(kwargs["text"])

    # 切换至新窗体
    def switch_to_new_current(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 关闭旧窗体
    def close_old_current(self, **kwargs):
        self.driver.close()

    # 切换至旧窗体
    def switch_to_old_current(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    # 切换至新窗体，并关闭旧窗体
    def switch_and_close(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 切换至Iframe窗体
    def switch_to_iframe(self, **kwargs):
        self.driver.switch_to.frame(self.locator(**kwargs))

    # 切换回默认窗体
    def switch_to_default(self, **kwargs):
        self.driver.switch_to.default_content()

    def assert_text(self,**kwargs):
        try:
            reality = self.locator(**kwargs).text
            assert reality == kwargs['expect']
            Logger().log().info("流程正确，断言成功！")
            return True
        except Exception as e:
            Logger().log().info("流程正确，断言失败！失败信息：{}".format(e))
            return False
    #unittest断言函数
    def get_element(self,loc_type,value):
        return self.driver.find_element(getattr(By,loc_type.upper()),value).text
