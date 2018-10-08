
class MyIterable(object):
    container = None

    def __init__(self):
        self._container = [1,2,3]

    def __iter__(self):
        # return iter(self._container)
        return MyIterator(self._container)


class MyIterator(object):

    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self._iterable[self._index]
            self._index += 1
            return result
        except IndexError:
            raise StopIteration



        setA = {'one', 'two', 'three'}