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
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if target > array[mid]:
            low = mid + 1
        elif target < array[mid]:
            high = mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    test_cases = [
        (([0, 5, 10, 11, 120], 120), 4),
        (([-1, 1, 2, 30], -1), 0),
        (([-10, 0, 99, 200], -11), -1),
        (([1, 8, 99, 201], 202), -1),
    ]

    for case in test_cases:
        a = case[0][0]
        t = case[0][1]
        r = case[1]

        print(f'search for {t} in {a}')
        result = binary_search(a, t)
        assert result == r
