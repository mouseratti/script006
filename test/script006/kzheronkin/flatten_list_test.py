import pytest
from script006.kzheronkin.lab2 import flatten_nested_list_in_list

_fixtures = [
    [
        [1,2,[3,4]],
    ]
]

def test_flatten_list():
    f = _fixtures[:]
    assert flatten_nested_list_in_list(f) == [1,2,3,4]
    assert f == _fixtures




