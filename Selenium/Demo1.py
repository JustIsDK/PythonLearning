from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  #此处是新的写法,很难记

browser.get('http://www.baidu.com')
search = browser.find_element(By.ID,'kw')
breakpoint()
search.send_keys('python')
breakpoint()
search.send_keys(Keys.ENTER)   #此处调用此方法会导致浏览器闪退
breakpoint()

