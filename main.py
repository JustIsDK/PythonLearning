import unittest
from testcases.test_fixture import TestFixture
def creat_suite():

    suite = unittest.TestSuite()
    suite.addTest(TestFixture('test_01'))
    suite.addTest(TestFixture('test_02'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = creat_suite()
    runner.run(suite)