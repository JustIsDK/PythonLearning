import unittest
class TestFixture(unittest.TestCase):

    def setUp(self) -> None:
        print('run setup ...')

    def tearDown(self) -> None:
        print("It's over")

    @classmethod
    def setUpClass(cls) -> None:
        print('before all case run ...')

    @classmethod
    def tearDownClass(cls) -> None:
        print('after all case run ...')

    def test_01(self):
        print('run test01')
        self.assertEqual(1,1)

    def test_02(self):
        print('run test02')
        self.assertTrue(True)

    def test_03(self):
        print('run test03')
        self.assertFalse(False)