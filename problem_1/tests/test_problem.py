from problem_1.p001 import multiple_of_dividers


def test_p001():
    assert multiple_of_dividers(10, [3, 5]) == 23
    assert multiple_of_dividers(11, [3, 5]) == 33
    assert multiple_of_dividers(12, [3, 5]) == 33
    assert multiple_of_dividers(2, [3, 5]) == 0
