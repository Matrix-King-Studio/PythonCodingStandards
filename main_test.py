"""
测试主函数
"""

import unittest

from main import is_number


class TestIsNumber(unittest.TestCase):
    def test_is_number(self):
        self.assertEqual(is_number(1), True)
        self.assertEqual(is_number("一"), True)
        self.assertEqual(is_number("haha"), False)


if __name__ == "__main__":
    unittest.main()
