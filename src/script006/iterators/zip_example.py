MAX_VALUE = 100000000

def with_iterators():
    integers = range(MAX_VALUE)
    i1 = i2 = iter(integers)
    assert i1 is i2
    yield from zip(i1, i2)
    # for value in zip(i1,i2):
    #     yield value
    #

def with_generators():
    integers = range(MAX_VALUE)
    return ((x, x+1) for x in integers if not x % 2)

def with_list_comprehensions():
    integers = range(MAX_VALUE)
    return [(x, x+1) for x in integers if not x % 2]

def process(value):
    pass
