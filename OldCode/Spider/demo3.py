import requests
import time
def downloadFile(name,url):
    headers = {'Proxy-Connection': 'keep-alive'}
    r = requests.get(url,stream=True,headers=headers)
    length = float(r.headers['Content-length'])
    f = open(name,'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk) # 写入文件
            count += len(chunk) #累加长度
            #计算时间 两秒打印一次
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
                time1 = time.time()
    f.close()


def formatFloat(num):
    return '{:.2f}'.format(num)


if __name__ == '__main__':
    dl = input('Please input your url: ')
    dwlurl = str(dl)
    name = str(input('Please input your filename: '))
    path = '/Users/dl00005ml/Downloads/'
    finalname = path + name

    downloadFile(finalname , dl)
