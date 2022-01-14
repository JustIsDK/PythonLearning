import unittest

class TestA(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('所有用例执行之前')
        cls.token='100'

    def setUp(self) -> None:
        print('每个测试方法执行之前')

    def tearDown(self) -> None:
        print('每个测试方法之后')

    @classmethod
    def tearDownClass(cls) -> None:
        print('所有用例之后')

    def test_1(self):
        print('test1')
        print(self.token)


class TestB(TestA):
    def test_b_1(self):
        print(self.token)

if __name__ == '__main__':
    unittest.main(verbosity=2)
