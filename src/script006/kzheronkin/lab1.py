def summary(n):
    if n >= 0:
        return sum(range(n +1 ))
    else:
        raise ValueError


def get_odd_numbers_from_interval(start_interval=0, end_interval=100):
    return [x for x in range(start_interval, end_interval) if x % 2 == 0]
