'''''
ss={'color':'green','point':'bmw'}
for key,value in ss.items():
    print('Key is '+key.upper())
    print('Value is '+str(value).upper())

for key in ss.values():
    print(key.title())

pussy={
    'name':'cat',
    'master':'DK'
}
gofy={
    'name':'dog',
    'master':'DC'
}
pets=[pussy,gofy]
for pet in pets:
    print(pet['master'],pet['name'])
'''
'''fp={
    'jack':['SH','NJ','SZ'],
    'nacy':['SC','CQ'],
    'Alice':['SY','BJ']
}
for ss,sss in fp.items():
    print('My Friends '+ss.title()+" love's city are: ")
    for ll in sss:
        print(ll.title()+'\n')'''
cities={'shanghai':{'cou':'china','people':'14','fact':'big'},'paries':{'cou':'French','people':'1','fact':'roman'},'tokyo':{'cou':'japan','people':'3','fact':'clean'}}
for citname,cityinfo in cities.items():
    print(citname.upper()+' 具有这些特征:\n')
    print("\tIt's has "+cityinfo['people']+' people\n')
    print("\tIt belong to "+cityinfo['cou'].title()+'\n')
    print("\tIt's has this special "+cityinfo['fact'].title()+'\n')
