from selenium import webdriver
import os
driver = webdriver.Chrome()

file_path = 'file:///C:\Users\Hzg\Desktop\upload.html'
driver.get(file_path)

driver.find_element_by_name("file").click()
os.system('C:\\Users\\Hzg\\Desktop\\test1.exe')

#driver.find_element_by_name("file").send_keys('D:\\XX.txt')

#driver.quit()
