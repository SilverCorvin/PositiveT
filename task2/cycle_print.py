"""
This script makes cycled print from multiple files

Example:
    $ python cycle_print.py test.txt test2.txt test3.txt
"""

import time
import sys
from itertools import cycle
from contextlib import ExitStack

__author__ = 'Ivan Povalyaev'
__version__ = 0.1


def get_filehandlers_cycle(filenames):
    """
    Infinite cycle generator

    Yields:
        _io.TextIOWrapper: file object
    Examples:
        >>> cycled = get_filehandler_cycle(['test.txt', 'test2.txt'])
        >>> next(cycled).name
        'test.txt'
        >>> next(cycled).name
        'test2.txt'
        >>> next(cycled).name
        'test.txt'
    """
    with ExitStack() as stack:
        files = (stack.enter_context(open(fname)) for fname in filenames)
        yield from cycle(file for file in files)


def print_line(fhandler):
    """
    Prints next line from opened file

    Args:
        fhandler (_io.TextIOWrapper): file object
    Yields:
        str: nextline from file
    Examples
    """
    while True:
        data = fhandler.readline().strip()
        if not data:
            fhandler.seek(0)
            data = fhandler.readline().strip()
        yield data


def _main():
    if len(sys.argv) < 2:
        print(sys.modules[__name__].__doc__)
        sys.exit(1)
    filenames = sys.argv[1:]
    for f_handler in get_filehandlers_cycle(filenames):
        print(next(print_line(f_handler)))
        time.sleep(0.4)


if __name__ == '__main__':
    _main()
