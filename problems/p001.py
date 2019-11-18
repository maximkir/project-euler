
def multiple_of_dividers(limit, dividers=[]):
    """
    Finds the sum of all the multiples of 3 or 5 below given limit.
    :param dividers:
    :param limit:
    :return:
    """
    assert limit > 0
    total = 0
    for n in range(1, limit):
        if any(_is_divided_by(divider, n) for divider in dividers):
            total += n
    return total


def _is_divided_by(x, n):
    return n % x == 0
