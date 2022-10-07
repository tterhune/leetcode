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
from timeit import timeit


def pal(s):
    return s[::-1] == s


def pal2(s):
    special = [',', ';', ':', '!']
    l = len(s)

    j = l - 1
    for i in range(0, l):
        print(f'{s[i]} and {s[j]}')

        while s[j] in special:
            j -= 1

        if s[i] in special:
            continue

        if s[i] != s[j]:
            return False
        j -= 1

    return True


if __name__ == '__main__':
    test_cases = [
        ('abba', True),
        ('abca', False),
        ('ab!;ba', True),
        ('racecar', True),
        ('foobar', False),
        ('Fghhgf', True),
    ]

    for case in test_cases:
        result = pal2(case[0])
        assert(result == case[1])
        print(f'{case[0]} palindrome? = {result}')
