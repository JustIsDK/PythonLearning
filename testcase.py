import unittest


def creat_smoke_testing():

    suit = unittest.TestSuite()

    loader = unittest.TestLoader()
    allTests = loader.discover(start_dir='testcases',pattern='test**.py')
    return allTests


if __name__ == '__main__':
    runner = unittest.TextTestRunner
    suite = creat_smoke_testing()
    runner.run(suite)
