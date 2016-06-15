#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com/")

link=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text("搜索设置").click()
time.sleep(1)
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)
print driver.switch_to_alert().accept()

driver.quit()
