"""
Create your own enumerate implementation in this module
https://docs.python.org/3/library/functions.html#enumerate
"""
from typing import (
    Iterable,
    Generator
)


def my_enumerate(i: Iterable, start: int = 0) -> Generator:
    input_len = len(i)

    for index in range(start, start + input_len):
        yield (index, i[index - start])


