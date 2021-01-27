#chromedriver各版本下载地址:http://chromedriver.storage.googleapis.com/index.html
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait

from  selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
import random
import time

'''------------------------------------------------设置header----------------------------------------'''
# 获取请求头对象，该对象用于设置用户向浏览器发送请求的请求头，比如ip代理设置浏览器代理设置及浏览器后台运行等等
chrome_options = Options()
#此处设置了浏览器代理为H5的，这样打开的页面就跟用手机访问的是一样的
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36")
# chrome_options.add_argument('--user-data-dir=C:/Users/28546/AppData/Local/Google/Chrome/User Data')#使用用户浏览器数据启动
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) #去掉正受自动化测试软件控制的提示语


chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("referer=https://www.zhipin.com/shanghai/")
# 此处代码设置浏览器为后端运行，不会呈现出来
# chrome_options.add_argument("--headless")

#使用代理ip来发请求
# chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")
'''--------------------------------------------------浏览器操作----------------------------------'''
#获取浏览器对象，这个就好比人双击chrome浏览器，其中1、executable_path：为chromedriver的路径 2、options:为请求头对象

browser = webdriver.Chrome(executable_path="C:\chromedriver.exe",options=chrome_options)
# browser.execute_script('Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});')
#打开浏览器

# url = "https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9W5Eadh&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F"
# browser.get(url=url)
browser.get("https://passport.alibaba.com/member/reg/enter_fill_email.htm?_regfrom=TB_ENTERPRISE&_lang=")
#浏览器最大/小化
browser.maximize_window()
# browser.minimize_window()

#获取网页源代码
# text = browser.page_source

#打开一个新的页面
# newwindow = 'window.open("https://www.baidu.com")'
# browser.execute_script(newwindow)  #通过执行js脚本来打开一个新的页面
# print(browser.window_handles)    #遍历打开的所有窗口句柄
# print(browser.current_window_handle) #查看当前页面句柄
# browser.switch_to.window(browser.window_handles[0]) #切换页面
# browser.close()    #关闭当前页面
'''------------------------------cookie操作-----------------------'''
# browser.add_cookie({"name":"test","value":"111111"}) #设置cookie
# browser.delete_all_cookies()
# browser.add_cookie({"name":"lastCity","value":"101020100"})
# browser.add_cookie({"name":"__c","value":"1578881583"})
# browser.add_cookie({"name":"__g","value":"-"})
# browser.add_cookie({"name":"Hm_lvt_194df3105ad7148dcf2b98a91b5e727a","value":"1578881583"})
# browser.add_cookie({"name":"__l","value":"l=%2Fwww.zhipin.com%2Fshanghai%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DIBYCElg2InhaLCPnxncuQ2zc93xIiq_0D0QMsdwDqEShPmm-r66Zh_Ir0idbvQqK%26wd%3D%26eqid%3Ded7391010018a58e000000055e1bd22a&friend_source=0&friend_source=0"})
# browser.add_cookie({"name":"JSESSIONID","value":'""'})
# browser.add_cookie({"name":"_uab_collina","value":"157888421120766492060183"})
# browser.add_cookie({"name":"__zp_stoken__","value":"357fKm%2FOlK%2BCYcOmu8JSarqolf2816dErbTZvArsZYQeXw9vI%2BDV%2FFAwg8ClcW5AwXDkFRVWSPkPckalpflNMachjua4ibtVyXK8oeMcUKaxyE0amYJAyqupK%2Fv3CmH914vZ"})
# browser.add_cookie({"name":"toUrl","value":"/"})
# browser.add_cookie({"name":"__a","value":"1117176.1578881583..1578881583.68.1.68.68"})
# browser.add_cookie({"name":"Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a","value":"1578972610"})

print(browser.get_cookies())
# cookies = browser.get_cookies() #遍历cookie
# browser.delete_cookie("test") #删除cookie
# browser.delete_all_cookies() # 删除所有cookie

'''------------------------------input框操作-----------------------'''
# label_element = browser.find_element_by_id("kw") #通过id查找元素
# label_element = browser.find_element_by_class_name("s_ipt") #通过类目查找元素
# label_element = browser.find_element_by_tag_name("")   #通常标签名称查找元素
# label_element = browser.find_element_by_name("wd").in    #通过name查找名称元素
# label_element = browser.find_element_by_xpath("//input[@id='kw']")  #通过xpath来查找元素

# button_element = browser.find_element_by_id("su")
# button_element.click()  #按钮点击动作
'''------------------------------select框--------------------------'''
# select_element = Select(browser.find_element_by_id("searchHotelLevelSelect"))
# for option in select_element.options:
#     print(option.text)   #打印文本
#     print(option.get_attribute("value")) #打印属性
# select_element.select_by_index(2) #通过文本选择
# select_element.select_by_value("3") #通过value选择
# select_element.select_by_visible_text("二星级以下/经济") #通过文本选择
'''-------------------------------元素等待（隐私等待和显示等待）----------'''
# 1、隐式等待
# slip_element = browser.implicitly_wait(3)
# browser.find_element_by_class_name("nc-lang-cnt")
#2、显示等待
# try:
#     slip_element = WebDriverWait(browser,10).until(
#         EC.presence_of_element_located((By.CLASS_NAME,"nc-lang-cnt1")) #这里还有其他各种定位方式，查看提供的方法说明即可
#     )
# except:
#     print("--------")

'''--------------------------------------元素拖拽（行为链）--------------------------'''
#https://signup.zhipin.com/?ka=header-register boss直聘的网站案例
# while True:
#     action_chains = ActionChains(browser)  # 创建一个行为链
#     spans = browser.find_elements_by_xpath("//span[@class='nc_iconfont btn_slide']")
#     try:
#         for span in spans:
#             if span.size.get("height") > 0:
#                 action_chains.drag_and_drop_by_offset(span,258,0).perform()
#                 break
#     except:
#         print('---')
#
#     browser.refresh()
#     time.sleep(3)

browser.quit()