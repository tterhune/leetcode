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


def target_sum(array: List[int], targetSum: int) -> List[List]:
    result = []

    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    result.append(sorted([array[i], array[j], array[k]]))
    return sorted(result)


if __name__ == '__main__':
    test_cases = [
        (
            [12, 3, 1, 2, -6, 5, -8, 6],
            0,
            [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
        ),
    ]

    for case in test_cases:
        nums = case[0]
        value = case[1]
        print(f'{nums} {value}')

        result = target_sum(nums, value)
        print(f'result => {result} {case[2]}')

        assert(result == case[2])
