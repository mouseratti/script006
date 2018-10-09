import pytest
from script006.examples.iterators import MyIterable


@pytest.fixture
def myiterable():
    return MyIterable()

@pytest.mark.skip
def test_myiterator(myiterable):
    iterator = iter(myiterable)
    container = myiterable.container
    with pytest.raises(StopIteration):
        index = 0
        while 1:
            assert next(iterator) == container[index]
            index+=1