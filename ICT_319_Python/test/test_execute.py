import unittest

from ICT_319_Python.src.MathLib import MathLib, OperatorNotSupportedException
from ICT_319_Python.src.MathRequest import MathRequest


class TestMathLib(unittest.TestCase):

    def setUp(self):
        pass

    def test_execute_add_get_result(self):
        #given
        math_request = MathRequest(3, 'add', 4)

        #when
        MathLib.execute(math_request)

        #then
        self.assertEqual(7, math_request.get_res())

    def test_execute_sub_get_result(self):
        # given
        math_request = MathRequest(3, 'sub', 4)

        # when
        MathLib.execute(math_request)

        # then
        self.assertEqual(-1, math_request.get_res())

    def test_execute_mul_get_result(self):
        # given
        math_request = MathRequest(3, 'mul', 4)

        # when
        MathLib.execute(math_request)

        # then
        self.assertEqual(12, math_request.get_res())

    def test_execute_div_get_result(self):
        # given
        math_request = MathRequest(3, 'div', 4)

        # when
        MathLib.execute(math_request)

        # then
        self.assertEqual(0.75, math_request.get_res())

    def test_execute_div_throw_exception(self):
        # given
        math_request = MathRequest(3, 'not_supported_operator', 4)

        # when # then
        self.assertRaises(OperatorNotSupportedException, MathLib.execute, math_request)

    def test_execute_pow_get_result(self):
        # given
        math_request = MathRequest(3, 'pow', 4)

        # when
        MathLib.execute(math_request)

        # then
        self.assertEqual(81, math_request.get_res())

    def test_execute_root_get_result(self):
        # given
        math_request = MathRequest(3, 'root', 4)

        # when
        MathLib.execute(math_request)

        # then
        self.assertEqual(1.32, math_request.get_res())

if __name__ == '__main__':
    unittest.main()