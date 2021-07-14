import requests

# res =  requests.get(url="http://httpbin.org/ip")

# res =  requests.get(url="https://www.imooc.com")

# res = requests.post(url="http://httpbin.org/post",data={"name":"imooc"})
#
# print(res.text)

# data = {"key1":"value1","key2":"value2"}
#
# res = requests.get(url="http://httpbin.org/get",params=data)
#
# print(res.url)
# print(res.headers)

# res = requests.get(url="https://www.imooc.com/static/img/index/logo2020.png")
# print(res.content)

res =  requests.get(url="http://httpbin.org/ip")

print(res.json()["origin"])
print(res.status_code)
print(res.request.headers)
