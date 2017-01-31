import time
from itertools import cycle
from contextlib import ExitStack


def get_filehandler_cycle(filenames):
    with ExitStack() as stack:
        files = (stack.enter_context(open(fname)) for fname in filenames)
        yield from cycle(file for file in files)


def print_line(fhandler):
    while True:
        data = fhandler.readline().strip()
        if not data:
            fhandler.seek(0)
            data = fhandler.readline().strip()
        yield data


if __name__ == '__main__':
    filenames = ('test.txt', 'test2.txt', 'test3.txt')
    for f_handler in get_filehandler_cycle(filenames):
        print(next(print_line(f_handler)))
        time.sleep(0.4)
