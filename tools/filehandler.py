import random
import csv

def random_phone():
    phone_frefix = ['13','14','15','16','17','18','19']
    phone_last = ''
    for x in range(9):
        # 生成随机的整数
        phone_last += str(random.randrange(10))

    return random.choices(phone_frefix)[0]+phone_last

if __name__ == '__main__':
    with open('phone.csv',mode='w',encoding='utf8',newline='') as f:
        headers = ['编号','手机号']
        writer = csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()

        phone_list = []
        counter = 0
        while counter<100:
            num = random_phone()
            if not num in phone_list:
                # f.write(num+"\n")
                writer.writerow({'编号':counter,'手机号':num})
                phone_list.append(num)
                counter+=1