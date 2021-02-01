# for i in range(0,10000):
#     print('12000')

import os
# filePath = 'D:\\我的坚果云\\文件\\工作\\东方福利\\2020\\1224\\太平\\费率表\\员工'
# print(os.listdir(filePath))


basepath = 'D:\\我的坚果云\\文件\\工作\\东方福利\\2020\\1224\\太平\\费率表\\子女\\不含身故'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)