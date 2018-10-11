import pytest
from script006.kzheronkin import get_odd_numbers_from_interval

fixtures = [
    ([5, 10], [6, 8]),
    ([-10, 10], [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8])
]

@pytest.mark.parametrize("input, expected", fixtures)
def test_get_odd_numbers_from_interval(input, expected):
    assert get_odd_numbers_from_interval(input[0], input[1]) == expected


def test_get_odd_numbers_from_interval_no_params():
    assert get_odd_numbers_from_interval() == [x for x in range(0, 100) if x % 2 == 0]


