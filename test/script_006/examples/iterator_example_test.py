import pytest
from script006.examples.iterators.iterator_example import iter_through
fixtures = [
    (
        {1,2,3},
        [1,2,3]
    ),
    (
        (x for x in range(1,4)),
        [1,2,3]
    ),
    (
        {1: "one", 2: "two", 3: "three"},
        [1, 2, 3]
    )
]

@pytest.mark.parametrize("input,expected", fixtures)
def test_iterator_example(input, expected):
    assert iter_through(input) == expected
