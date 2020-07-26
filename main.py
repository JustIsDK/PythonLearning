import unittest
from testcases.test_fixture import TestFixture
from testcases.test_demo import TestStringMethods
# def creat_suite():
#
#     suite = unittest.TestSuite()
#     suite.addTest(TestFixture('test_01'))
#     suite.addTest(TestFixture('test_02'))
#     return suite

def creat_suite_CI():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestFixture)
    tests_02 = loader.loadTestsFromTestCase(TestStringMethods)
    # print(tests)
    # suite.addTests([TestFixture('test_01'),
    #                TestFixture('test_02'),
    #                TestFixture('test_03')])
    suite.addTests([tests,tests_02])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = creat_suite_CI()
    runner.run(suite)