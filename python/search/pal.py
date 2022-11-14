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


def pal3(s, idx):
    # start from middle and work out
    i = j = idx
    p_len = 0

    while i > 0 and j < len(s):
        if s[i] == s[j]:
            i -= 1
            j += 1
            p_len += 2
        else:
            return p_len

    # if p_len // 2 != 0:
    #     p_len += 1

    return p_len


if __name__ == '__main__':
    test_cases = [
        ('abba', True),
        ('abca', False),
        ('ab!;ba', True),
        ('racecar', True),
        ('foobar', False),
        ('Fghhgf', True),
    ]

    s = 'xyzabbabba'
    print(f'{s}')
    max_p = 0
    mid_i = 0
    for idx in range(1, len(s)):
        plen = pal3(s, idx)
        if plen > max_p:
            print(f'{idx} => {plen}')
            mid_i = idx
            max_p = plen

    half = max_p // 2

    end_i = mid_i + half
    start_i = mid_i - half

    print(f'{start_i} {end_i}')
    print(s[start_i:end_i])

    for case in test_cases:
        result = pal2(case[0])
        assert(result == case[1])
        print(f'{case[0]} palindrome? = {result}')
