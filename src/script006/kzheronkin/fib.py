import typing


def gen_fib(n: int) -> typing.Generator:
    (prev, curr) = (0, 1)
    for i in range(n):
        prev, curr = curr, prev + curr
        yield prev


def func_fib(n: int) -> typing.List:
    (prev, curr) = (0, 1)
    fib_list = list()
    for i in range(n):
        prev, curr = curr, prev + curr
        fib_list += [prev]
    return fib_list
