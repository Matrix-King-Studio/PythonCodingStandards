"""
测试主函数
"""

import unittest

from main import is_number


class TestIsNumber(unittest.TestCase):
    def test_is_number_1(self):
        self.assertEqual(is_number(1), True)

    def test_is_number_2(self):
        self.assertEqual(is_number("一"), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
