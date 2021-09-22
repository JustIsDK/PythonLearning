from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path="D:\Program Files\Python\chromedriver.exe")
driver.get("https://fuman-admin-test.dongfangfuli.com/")
time.sleep(1)
driver.find_element_by_id('account_login_tab').click
driver.find_element_by_id('login_account').input('admin')
driver.find_element_by_id('login_password').input('123456')
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/section/header/ul/li[4]').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/section/aside/div/ul/li[2]').click()
time.sleep(1)
selector = Select(driver.find_element_by_id('companyName').imput('bfd'))
selector.select_by_value('bfd')
driver.find_element_by_xpath('//*[@id="app"]/div/section[2]/div/div[2]/div/form/div[5]/div/div/div/button').click


