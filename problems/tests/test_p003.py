from problems.p003 import largest_prime_factor


def test_largest_prime_factor():
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(600851475143) == 6857
