from utils.common import next_prime


def largest_prime_factor(n):
    """
    :param n:
    :return: the largest prime factor of the given number
    """
    assert isinstance(n, int)
    return _find_largest_prime(2, n)


def _find_largest_prime(divider, num):

    if num == 1:    # recursion stop condition
        return divider

    if num % divider == 0:  # divider is a prime factor of num
        return _find_largest_prime(divider, num // divider)
    else:
        return _find_largest_prime(next_prime(divider), num)
