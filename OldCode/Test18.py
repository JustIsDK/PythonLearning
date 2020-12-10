#为配置保险产品的产品因子写的小循环，第一次体会到用代码解决了实际的问题，降低了手工的成本

a = []
for i in range(1,51):
    a.append('__$'+str(i*10))

for b in a:
    print(str(b),end='')