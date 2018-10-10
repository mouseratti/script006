import itertools
from string import digits, ascii_lowercase

def chain():
    i1 = (_ for _ in ('one', 'two', 'three'))
    i2 = [letter for letter in ascii_lowercase]
    i3 = []
    yield from itertools.chain(i1,i2,i3)


def count():
    yield from itertools.count(20, 5)


if __name__ == '__main__':
    g1 = chain()
    while True:
        try:
            print(next(g1))
        except StopIteration:
            break

    g2 = count()
    print([next(g2) for _ in range(3)])
    print(next(g2))