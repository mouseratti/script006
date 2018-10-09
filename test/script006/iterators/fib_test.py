import pytest
import types
from script006.iterators import gen_fib, func_fib

test_fibonacci_function_and_generator_fixtures = [
    (1, [1, ]),
    (2, [1, 1],),
    (3, [1, 1, 2],),
    (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    (20, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ]),
]


@pytest.mark.parametrize("input, expected", test_fibonacci_function_and_generator_fixtures)
def test_fibonacci_function_and_generator(input, expected):
    assert list(gen_fib(input)) == func_fib(input) == expected


def test_gen_fib():
    test_fibonacci_sequence = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,)
    n = len(test_fibonacci_sequence)
    result = gen_fib(n)
    assert isinstance(result, types.GeneratorType)
    for value in test_fibonacci_sequence:
        assert next(result) == value


def test_func_fib():
    test_fibonacci_sequence = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,)
    n = len(test_fibonacci_sequence)
    result = func_fib(n)
    assert isinstance(result, list)
    for position, value in enumerate(test_fibonacci_sequence):
        assert result[position] == test_fibonacci_sequence[position] == value
