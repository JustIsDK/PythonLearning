import requests
from bs4 import BeautifulSoup as bfs
import  os


def firststep(url,headers,baseurl):
    r = requests.get(url=url, headers=headers)
    #请求url获取html
    soup = bfs(r.text, 'lxml')
    #用lxml解析成为对象
    data = soup.select('td >div[class="attachlist"] >table >tr >td >a[rel = "nofollow"]')
    #使用css  selector找到目标列表
    dwl = []
    #新建空列表用来存放下载链接
    for i in range(len(data)):
        #循环取列表中的项
        newurl = baseurl + str(data[i].get('href'))
        #获取href属性的值，也就是种子的链接url
        # filename = str(data[i].text[61:63])
        #截取种子的名字，用作展示，不过我没有存下来
        dwl.append(newurl)
        #为列表增加值
    return dwl
    #返回下载列表



def nextstep(url,baseurl):
    #新建下载方法
    re = requests.get(url=url)
    soup1 = bfs(re.text,'lxml')
    data = soup1.find_all('a')
    downurl = str(baseurl) + str(data[-3].get('href'))
    name = soup1.find_all('dd')
    trrname = str(name[0].text)
    #上面这些还是老样子，请求，返回，转换html对象等等
    r = requests.get(downurl)
    #用request下载，这样下载会先存到内存中
    with open(trrname, "wb") as f:
        #这样才能保存到本地
        f.write(r.content)
    f.close()
    print("Sucessful to download： " + trrname)
    #输出下载成功的提示



def main():
    #主方法，用来调用上面两个方法
    baseurl = 'https://btbtt16.com/'
    url = 'https://btbtt16.com/thread-index-fid-981-tid-4497137.htm'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    #基本参数都放在这个里面

    dwl = []
    #新建下载链接列表用来放方法一返回的列表

    dwl = firststep(url=url,headers=headers,baseurl=baseurl)
    #已经拿到返回

    for i in range(len(dwl)):
        #把dwl中的每一个链接传入到方法二中，用方法二去一个个下载
        nextstep(url=dwl[i],baseurl=baseurl)

    print('All Download Complete')
    #成功，撒花


main()