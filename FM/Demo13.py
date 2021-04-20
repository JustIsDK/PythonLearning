from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
tc = webdriver.Chrome(executable_path="G:\Code\chromedriver.exe")
tc.get('https://www.baidu.com/')
tc.find_element_by_id('kw').send_keys('测试')
time.sleep(1)
tc.find_element_by_id('su').click()
tc.close()