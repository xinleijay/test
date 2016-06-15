from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.add_cookie({'name': 'key-aaaaaa', 'value': 'value-bbbbbbb'})
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))
#driver.delete_cookie('key-aaaaaa')
#cookie = driver.get_cookies()
#print(cookie)
driver.quit()