import unittest
from math import sqrt, floor
from random import randint


def is_prime_slow(n):
    """
    Check if a number is prime using a slow method.
    :param n: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_fast(n, k=5):  # Miller-Rabin
    """
    Check if a number is prime using the fast Miller-Rabin method.
    :param n: The number to check.
    :param k: The number of iterations to perform.
    :return: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n):
    """
    Find the next prime number after a given number.
    :param n: The number to start from.
    :return: The next prime number.
    """
    if n < 2:
        return 2
    prime = n
    found = False
    while not found:
        prime += 1
        if is_prime_fast(prime):
            found = True
    return prime


class TestPrimeLibrary(unittest.TestCase):
    """
    Unit tests for the prime library.
    """

    def test_is_prime_slow(self):
        """
        Test the slow prime checking function.
        """
        self.assertFalse(is_prime_slow(1))
        self.assertTrue(is_prime_slow(2))
        self.assertFalse(is_prime_slow(4))
        self.assertTrue(is_prime_slow(17))

    def test_is_prime_fast(self):
        """
        Test the fast prime checking function.
        """
        self.assertFalse(is_prime_fast(1))
        self.assertTrue(is_prime_fast(2))
        self.assertFalse(is_prime_fast(4))
        self.assertTrue(is_prime_fast(17))

    def test_next_prime(self):
        """
        Test the next prime function.
        """
        self.assertEqual(next_prime(1), 2)
        self.assertEqual(next_prime(2), 3)
        self.assertEqual(next_prime(17), 19)

    def test_non_integer_input(self):
        """
        Test that the functions raise a TypeError when given a non-integer input.
        """
        with self.assertRaises(TypeError):
            is_prime_slow(3.5)
        with self.assertRaises(TypeError):
            next_prime(3.5)


if __name__ == '__main__':
    unittest.main()
