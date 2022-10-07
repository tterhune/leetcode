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
from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    array_len = len(arr)

    if array_len <= 1:
        return [-1]

    max = arr[array_len - 1]
    for i in range(array_len - 2, -1, -1):
        tmp = arr[i]
        arr[i] = max
        if tmp > max:
            max = tmp

    arr[array_len - 1] = -1
    return arr


if __name__ == '__main__':
    test_cases = [
        ([57010,40840,69871,14425,70605], [70605,70605,70605,70605,-1]),
        ([17,18,5,4,6,1], [18,6,6,6,1,-1])
    ]

    for case in test_cases:
        nums = case[0]
        print(f'{nums}')

        result = replace_elements(nums)
        print(f'result => {result} {case[1]}')
        assert(result == case[1])
