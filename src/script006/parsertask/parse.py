from collections import defaultdict
import typing
import re
from time import time

_TOP_STRINGS_COUNT = 30
_FILENAME = '/home/mkoshel/dev/script006.git/resources/logsample.log'
_PATTERN = re.compile("""(\d{2,4}-\d{1,2}-\d{1,2})\s(\d{2}\:\d{2}\:[\d\.]{1,6})\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\[.*?\])\s(\-)""")


def parse_url(line: str, pattern) -> str:
    """
    line should be like
    2018-10-16 09:33:21.796 [Посылки_ручная сортировка] [МОСКОВСКИЙ АСЦ ЦЕХ ПОСЫЛОК] [Чувина Е.Е.] [10.128.254.96] [/auth/user] [GET] [2 ms] -"""
    try:
        url = pattern.match(line).group(7)
    except:
        url = line
    return url


def read_file(filename: str) -> typing.Generator:
    with open(filename, "rt") as f:
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                break

if __name__ == '__main__':
    lin3counter = 0
    start = time()
    storage = defaultdict(int)
    for line in read_file(_FILENAME):
        lin3counter += 1
        url = parse_url(line, _PATTERN)
        storage[url] +=1
        # print(lin3counter, url)
    for line in sorted(storage, key=lambda x: storage[x], reverse=True)[:_TOP_STRINGS_COUNT]:
        print(line, storage[line])
    end = time()
    print(end - start)