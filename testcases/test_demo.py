import unittest

class TestStringMethods(unittest.TestCase):

    def add(self):
        # 不会当作测试用例来执行，这个只是一个普通的方法而已
        print('helloworld')

    def test_upper(self):
        # 判断字符串upper转换为大写 'foo'.upper() ==  'FOO'
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        # 大写 'FOO'.isupper() == True
        self.assertTrue('FOO'.isupper())
        # 判断不为大写 'Foo'.isupper() == False
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # 判断程序抛出异常信息 s.split(2) 抛出 TypeError 异常信息
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # 显示详细的测试结果
    unittest.main(verbosity=2)