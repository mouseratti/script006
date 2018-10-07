import pytest
from script006.labs.mkoshel import module_summary

fixtures = [
    (0, 0),
    (5, 15),
    (1, 1),
    (3,6),
    (4,10)
]

@pytest.mark.parametrize("input, expected", fixtures)
def test_summary(input, expected):
    assert module_summary(input) == expected


def test_summary_raises():
    with pytest.raises(ValueError):
        module_summary(-1)

