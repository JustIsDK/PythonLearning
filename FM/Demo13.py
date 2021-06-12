import pymysql
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
tc = webdriver.Chrome(executable_path="/Users/dk/chromedriver")
tc.get('https://www.baidu.com/')
print('打开网页成功')
tc.find_element_by_id('kw').send_keys('这个是 UI 自动化输入的文字')
print('输入测试成功')
time.sleep(2)
print('间歇性休眠成功')
tc.find_element_by_id('su').click()
print('点击搜索成功')
time.sleep(2)
tc.close()



# db = pymysql.connect(
#     host='rm-uf6155459cp80g165.mysql.rds.aliyuncs.com',
#     port=3306,
#     user='fuman',
#     passwd='fumandffl',
#     db='fuman_group_apply'
# )
#
# dblink = db.cursor()
#
# sql = "SELECT order_no,order_step,order_status,self_opt_start_time,self_opt_end_time,request_no  " \
#       "from `t_group_order` WHERE id = '412b9ef7d59447a49f825ad4ceb125dd';"
#
# dblink.execute(sql)
#
# results = dblink.fetchall()
#
# print(results)
