from utils.common import is_prime, next_prime


def test_is_prime():
    assert all(is_prime(n) for n in (7, 4049, 18869, 19319, 26261))
    assert not any(is_prime(n) for n in (35, 36, 49, 64))


def test_next_prime():
    assert next_prime(3) == 5
    assert next_prime(29) == 31
