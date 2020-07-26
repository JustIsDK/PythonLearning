import unittest
import testcases.test_demo as t1
from testcases.test_fixture import TestFixture
from testcases.test_demo import TestStringMethods
from testcases.test_filehandler import TestFileHandler
# def creat_suite():
#
#     suite = unittest.TestSuite()
#     suite.addTest(TestFixture('test_01'))
#     suite.addTest(TestFixture('test_02'))
#     return suite

def creat_suite_CI():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    #从单个测试用例来加载
    tests = loader.loadTestsFromTestCase(TestFixture)
    tests_02 = loader.loadTestsFromTestCase(TestStringMethods)
    tests_03 = loader.loadTestsFromTestCase(TestFileHandler)
    # print(tests)
    # suite.addTests([TestFixture('test_01'),
    #                TestFixture('test_02'),
    #                TestFixture('test_03')])
    suite.addTests([tests,tests_02,tests_03])
    return suite

def creat_suite_CI3():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    #从方法名来加载
    tests = loader.loadTestsFromName('testcases.test_demo')
    suite.addTests(tests)
    return suite

def creat_suite_CI2():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    #从模块名来加载
    tests = loader.loadTestsFromModule(t1)
    suite.addTests(tests)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = creat_suite_CI3()
    runner.run(suite)