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

def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    for i in range(0, 10):
        result = fib(i)
        print(f'{result}')
