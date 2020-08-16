from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path="D:\Program Files\Python37\chromedriver.exe")
driver.get("https://www.baidu.com/")
time.sleep(1)
driver.find_element_by_name('wd').send_keys('1')
driver.find_element_by_id('su').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()


