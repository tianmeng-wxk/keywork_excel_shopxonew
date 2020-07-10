import unittest,time
from selenium import webdriver
from keywork.webui_keywork import WebUIKeys
from log.log import Logger
from common.common import SendEmail
from ddt import ddt,file_data

@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wk = WebUIKeys("CHR")
        cls.wk.driver.implicitly_wait(10)
        cls.log = Logger().log()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.send_email=SendEmail().send_email(r"D:\keywork_shopxo\report\2020_07_07_05_08_43_html_report.html")
        cls.log.info("---------测试完成----------")
        cls.wk.quit()


    #登录v1.0
    # @file_data('../config/login.yaml')
    # def test_01_login(cls, **data):
    #     for value in data["login"]:
    #         cls.log.info("调用的关键字：{}".format(value["name"]))
    #         if value["name"] == 'visit':
    #             getattr(cls.wk,value["name"])(value["url"])
    #         elif value["name"] == 'click':
    #             getattr(cls.wk, value["name"])(value["loc_type"],value["value"])
    #         elif value["name"] == 'sleep':
    #             getattr(cls.wk, value["name"])(value["time"])
    #         elif value["name"] == 'input':
    #             getattr(cls.wk, value["name"])(value["loc_type"],value["value"],value["txt"])
    #         elif value["name"]=="assert_text":
    #             getattr(cls.wk, value["name"])(value["loc_type"], value["value"], value["expect"])
    #
    #         else:
    #             pass
        # cls.wk.visit("http://39.98.138.157/shopxo/index.php")
        # cls.wk.click("xpath", "//a[text()='登录']")
        # cls.wk.sleep(1)
        # cls.wk.input("name", "accounts", "666666")
        # cls.wk.input("name", "pwd", "111111")
        # cls.wk.click("xpath", "/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button")
        # cls.wk.sleep(3)
        # cls.assertEqual("退出", cls.wk.get_element("xpath","//a[text()='退出']"),msg="登录失败")


    #搜索
    # def test_02_search(cls):
    #     cls.wk.input('xpath', '//*[@id="search-input"]', "手机")
    #     cls.wk.click("xpath",'//*[@id="ai-topsearch"]')
    #     cls.wk.sleep(5)
    #     print(cls.wk.get_element("xpath", "/html/body/div[4]/div/ul"))
    #     cls.assertIn("手机", cls.wk.get_element("xpath", "/html/body/div[4]/div/ul"), msg="搜索商品失败")


    #加入购物车
    # def test_03_add_shop_cart(cls):
    #     # el = cls.wk.driver.find_element_by_xpath('"/html/body/div[4]/div/ul/li[1]/div/a/img"')
    #     # js = 'argument[0].scrollIntoView()'
    #     # cls.wk.driver.execute_script(js, el).click()
    #     cls.wk.click("xpath", "/html/body/div[4]/div/ul/li[1]/div/a/img")
    #     cls.wk.sleep(2)
    #     headle = cls.wk.driver.window_handles
    #     cls.wk.driver.close()
    #     cls.wk.driver.switch_to.window(headle[2])
    #     cls.wk.sleep(2)
    #     #未添加购物车前显示已添加在购物车不同商品的数量
    #     index = int(cls.wk.get_element("xpath", "/html/body/div[1]/div/ul[2]/div[4]/div/a/strong"))
    #     cls.log.info('添加商品到购物车前，购物车已存在的商品数量:{}'.format(index))
    #     cls.wk.click('xpath', '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[2]')
    #     cls.wk.sleep(1)
    #     cls.wk.click('xpath', '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[2]')
    #     cls.wk.sleep(1)
    #     cls.wk.click('xpath', '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[2]')
    #     cls.wk.sleep(1)
    #     cls.wk.input('xpath', '//*[@id="text_box"]', '1')
    #     cls.wk.click('xpath', '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')
    #     cls.wk.sleep(2)
    #     #清空购物车再做这个断言，下次换个断言方式
    #     cls.log.info('添加商品到购物车后，购物车已更新的商品数量:{}'.format(cls.wk.get_element("xpath", "/html/body/div[1]/div/ul[2]/div[4]/div/a/strong")))
    #     cls.assertEqual(index+1, int(cls.wk.get_element("xpath", "/html/body/div[1]/div/ul[2]/div[4]/div/a/strong")), msg='添加购物车失败')

if __name__ == '__main__':
    unittest.main()