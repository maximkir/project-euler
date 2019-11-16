
def sum_even_fibonacci_numbers(limit):
    """
    Finds the sum of the even-valued terms in the Fibonacci sequence
    :param limit:
    :return:
    """
    a, b = 1, 2
    total = 0
    while a < limit:
        if a % 2 == 0:
            total += a
        tmp = a
        a = b
        b = a + tmp
    return total
