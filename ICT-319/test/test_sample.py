import unittest

from src.MathRequest import MathRequest

class TestMathRequest(unittest.TestCase):

    def setUp(self):
        self.ope1 = 3
        self.operator = '+'
        self.ope2 = 5
        self.mathRequest = MathRequest(self.ope1, self.operator, self.ope2)

    def test_get_ope1(self):
        self.assertEqual(self.ope1, self.mathRequest.get_ope1())

    def test_get_oper(self):
        self.assertEqual( self.operator, self.mathRequest.get_operator())

    def test_get_ope2(self):
        self.assertEqual(self.ope2, self.mathRequest.get_ope2())

    def test_to_string(self):
        self.assertEqual("3 + 5 = None", self.mathRequest.to_string())

if __name__ == '__main__':
    unittest.main()