# -*- coding: utf-8 -*-

import functools
import time


def trace(func):
    print('In trace() decorator function')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'In wrapper() calling func(): {func.__name__}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'In wrapper() func() returned, took: {round(end-start, 3)}s')
        return result

    return wrapper


@trace
def do_stuff():
    print('In do_stuff()')
    time.sleep(2)


if __name__ == '__main__':
    print('Entered main...')
    do_stuff()
