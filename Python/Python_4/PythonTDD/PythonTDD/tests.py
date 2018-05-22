import unittest
from funcs import is_prime

class FuncsTestcase(unittest.TestCase):
    """Tests for funcs.py"""

    def test_is_negative_prime(self):
        """#T1 Are negative numbers between (-10 and -1)
           determined to be primes?"""
        for i in range(-10, 0):
            self.assertFalse(is_prime(i))

    def test_alpha_inputs(self):
        """#T2 Test alphabetic input - a"""
        self.assertRaises(TypeError, lambda: is_prime('a'))

    def test_is_zero_prime(self):
        """#T3 Is 0 considered as a prime number?"""
        self.assertFalse(is_prime(0))

    def test_positive_prime_numbers(self):
        """#T4 Tests whether 3 5 7 are prime numbers"""
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_is_one_prime(self):
        """#T5 Is 1 prime?"""
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()