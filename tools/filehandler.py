"""
文件处理类，在这个文件处理类型添加对csv文件，excel文件处理的方法
"""
import csv
import os
data_dir = os.path.join(os.path.dirname(__file__),'../data')
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

class FileHandler:
    def __init__(self,filename):
        self.filepath = os.path.join(data_dir, filename)

    def readcsv(self):
        """
        从csv文件中读取数据
        :return: reader
        """
        if not os.path.exists(self.filepath):
            return None
        data=[]
        with open(self.filepath, mode='r', encoding='utf8') as f:
            reader = csv.reader(f)
            for line in reader:
                data.append(line)
        return data


    def writecsv(self,listdata):
        """
        写入数据到csv文件中
        :param listdata: 写入文件的数据 [[],[]] 二维的list
        :return:
        """
        # 如果这个文件所在的目录不存在，创建目录
        if not os.path.exists(os.path.dirname(self.filepath)):
            # TODO 创建多级目录
            os.makedirs(os.path.dirname(self.filepath))
            # os.mkdir(os.path.dirname(self.filepath))

        with open(self.filepath, mode='w', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            # 需要使用到list 数据
            for line in listdata:
                writer.writerow(line)

if __name__ == '__main__':
    file = FileHandler('data.csv')
    file.writecsv([['id', 'name'], ['1', 'xiaozhang'], ['2', 'xiaoming']])
