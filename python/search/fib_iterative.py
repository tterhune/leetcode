# -*- coding: utf-8 -*-
##########################################################################
#
# Copyright (C) 2022 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
# The contents of this software are proprietary and confidential
# to the Hewlett Packard Enterprise Development LP.  No part of this
# program may be photocopied, reproduced, or translated into another
# programming language without prior written consent of the
# Hewlett Packard Enterprise Development LP.
#
##########################################################################

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# f(n) = f(n-2) + f(n-1)
def fib(n: int) -> int:
    if n == 0:
        return n
    previous = 0
    current = 1

    for _ in range(1, n):
        tmp = current
        current = previous + current
        previous = tmp

        # tuple unpacking to not need tmp
        # previous, current = next, previous + current
    return current


if __name__ == '__main__':
    for i in range(0, 10):
        result = fib(i)
        print(f'{result}')
    result = fib(50)
    print(f'fib(50) = {result}')
