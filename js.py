from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/s?wd=loadrunner")

text = "selenium"
js = "var temp=document.getElementById('kw');temp.value='" + text + "';"
driver.execute_script(js)
js2 = "var cli=document.getElementById('su'); cli.click();"
driver.execute_script(js2)
sleep(10)

driver.quit()