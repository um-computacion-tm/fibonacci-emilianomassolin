
 

import unittest
from fibonacci import fibonacci

class TestFibo(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, fibonacci(1))
        
    def test_2(self):
        self.assertEqual(1, fibonacci(2))

    def test_3(self):
        self.assertEqual(2, fibonacci(3))

    def test_4(self):
        self.assertEqual(3, fibonacci(4))

    def test_5(self):
        self.assertEqual(5, fibonacci(5))

    def test_6(self):
        self.assertEqual(8, fibonacci(6))

    def test_15(self):
        self.assertEqual(610, fibonacci(15))

    def test_16(self):
        self.assertEqual(987, fibonacci(16))

    def test_17(self):
        self.assertEqual(1597, fibonacci(17))

    def test_18(self):
        self.assertEqual(2584, fibonacci(18))

    def test_19(self):
        self.assertEqual(4181, fibonacci(19))

    def test_20(self):
        self.assertEqual(6765, fibonacci(20))

if __name__ == '__main__':
    unittest.main()