#coding=utf-8
from selenium import webdriver
from time import sleep
import logging
logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)
#截取当前窗口,并指定图片的保存位置
#driver.get_screenshot_as_file("C:\\Users\\Hzg\\Desktop\\test.jpg")
driver.quit()