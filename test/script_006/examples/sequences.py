def list_comprehensions():
    """
    docstring for list_comprehensions
    :returns None
    """
    # list comprehensions
    r10 = range(10)
    mapa = map(lambda x: x if x %2 ==0 else x+1,r10)
    l1 = [x for x in mapa]
    l11 = [x for x in map(lambda x: x if x %2 ==0 else x+1,range(10))]
    #assert l1 != l11


    filter1 = filter(lambda x: True if x %2 > 0 else False, r10)
    l2 = [_ for _ in filter1]
    print(l2)
    l22 = filter(None, [lambda x: x if x % 2 >0 else None for x in range(10)])
    # assert list(l22) == l2


    return

def set_comprehensions():
    names = [
        'Linda',
        'Masha' ,
        'Ian',
        'm',
        'linda',
        'ian',
    ]
    set1 = {'{}{}'.format(x[0].upper(), x[1:].lower()) for x in names if len(x) > 1}
    print(set1)



def generators():
    def gf1():
        yield "one"
        yield "two"
        yield "three"

    l1 = [print(_) for _ in gf1()]

    def gf2():
        print("new gf2 created!")
        cntr = 0
        while True:
            cntr += 1
            yield cntr
            if cntr > 3: break

    g2 = gf2()

    try:
        while True:
            print(next(g2))
    except Exception as e:
        print("Error is {}".format(type(e)))





def main():
    list_comprehensions()
    # lk = list_comprehensions
    set_comprehensions()
    generators()



if __name__ == '__main__':
    print(__name__)
    main()