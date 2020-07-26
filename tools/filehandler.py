with open('phone_num.csv',mode='w',encoding='utf8',newline='') as f:
    headers = ['编号','手机号码']
    writer = csv.DictWriter(f,fieldnames=headers)
    # 写入表头
    writer.writeheader()

    writer.writerow({"编号":1,'手机号码':13211112222})