# 包：py2-ipaddress==3.4.1
import ipaddress
a = ipaddress.IPv4Address('172.16.16.203')
b = ipaddress.IPv4Network('172.18.16.75')
if a in b:
    print('同一网段')
else:
    print('不是同一网段')

# ip地址a，在b网段中