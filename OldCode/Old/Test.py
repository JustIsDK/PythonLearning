#name=input('Please input your name: ')
#print('Hello '+name+' nice to meet you')
#print(name.lower())
#print(name.upper())
#print(name.title())
#name='   dk   '
#print('Hello, \n'+'\t'+name.lstrip()+name.rstrip()+name.strip()+'''\nI'm your friend''' )
ss=[sss**3 for sss in range(1,10)]
print(ss)
print(ss[1:4])
sss=sorted(ss,reverse=True)
print(sss[:3])
print(ss[3:6])
print(ss[6:])
s=ss[:]
s.append('s')
ss.append('ss')
print('This is s:')
for q in s:
    print(q)
print('This is ss:')
for w in ss:
    print(w)