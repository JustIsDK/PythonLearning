import os
import unittest

from tools.filehandler import FileHandler


class TestFileHandler(unittest.TestCase):

    def test_readcsv(self):
        f = FileHandler('phone.csv')
        data = f.readcsv()
        # 判断文件中的数据长度为 100
        self.assertEqual(len(data), 100)

    def test_writecsv(self):
        f = FileHandler('data.csv')
        # 如果存在data.csv文件，先把csv文件删除
        if os.path.exists(f.filepath):
            os.remove(f.filepath)
        # 文件写入
        f.writecsv([['1', 'xiaoming'], ['2', 'xiaowang']])

        # 添加断言 文件写入成功 验证文件已经创建好
        self.assertTrue(os.path.exists(f.filepath))
        # 读取文件内容，文件内容应该与写入的文件内容保持一致
        result = f.readcsv()
        self.assertEqual(result, [['1', 'xiaoming'], ['2', 'xiaowang']])


if __name__ == '__main__':
    unittest.main(verbosity=2)
