# -*- coding: utf-8 -*-

# Factorial
#
# f(0) = 0! = 1
#
# n! = f(n) = n * n-1 * n-2 * n-3 * ... * 1
#
# n! = n * (n-1)!
#

def fact2(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    # result = subsets([1, 2, 3])
    tests = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
    ]
    for t in tests:
        result = fact(t[0])
        print(f'fact({t[0]}) = {result}')
        assert t[1] == result

    for t in tests:
        result = fact2(t[0])
        print(f'fact({t[0]}) = {result}')
        assert t[1] == result
