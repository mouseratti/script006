

def summary(n=0):
    if n < 0: raise ValueError
    return sum (range(0, n+1))