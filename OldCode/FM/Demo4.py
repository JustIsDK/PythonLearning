import unittest
import requests
class NodeBlogTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_interface_result(self):
        req = requests.get(F"{}"{url})
        data = req.json()
        self.assertEqual(data["success"],True)


    def tearDown(self):
        pass


if __name__ == "__main__":
        unittest.main()
