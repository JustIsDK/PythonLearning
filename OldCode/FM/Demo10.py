import yaml
import unittest
import os,sys

is_win32 = sys.platform == 'win32'

need_windows = unittest.skipUnless(is_win32,'需要操作系统为Windows')

class Test1(unittest.TestCase):

    def test01(self):
        assert True
        print('test01成功了\n')

    @need_windows
    def test02(self):
        assert True
        print('这条跳过了\n')

    @unittest.skip('这次不执行')
    def test03(self):
        assert False

if __name__ == '__main__':
    unittest.main(verbosity=2)
