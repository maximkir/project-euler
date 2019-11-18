import math


def is_prime(n):
    """
    Checks whether the given integer number is a prime
    :param n:
    :return:
    """
    assert isinstance(n, int) and n > 0, 'A prime number must be a positive integer'
    return not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))


def next_prime(n):
    """

    :param n: an integer
    :return: next prime number after a given number
    """
    assert isinstance(n, int) and n > 0, 'The function expects for a positive integer value'
    prime_candidate = n + 1
    while not is_prime(prime_candidate):
        prime_candidate += 1
    return prime_candidate
