import unittest

from ICT114.ICT_114_PYTHON.Hashage_package.HashRequest import HashRequest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.user_input = "auto"
        self.choice = "auto"
        self.HashRequest = HashRequest(self.user_input)

    def test_get_user_input(self):
        self.assertEqual(self.user_input, self.HashRequest.get_user_input())

    def test_get_choice(self):
        self.assertEqual(self.choice, self.HashRequest.get_choice())# add assertion here


if __name__ == '__main__':
    unittest.main()
