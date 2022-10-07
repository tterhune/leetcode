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


def target_sum(array: List[int], targetSum: int) -> List[int]:
    # use dictionary to store difference between
    # the current value and the targetSum
    # targetSum = difference + i
    differences = {}
    for i in array:
        difference = targetSum - i
        other_value = differences.get(difference)
        if other_value is None:
            # not found
            differences[i] = difference
        else:
            # We found an entry that will sum to the target
            return [i, difference]
    return []


if __name__ == '__main__':
    test_cases = [
        (([3, 5, -4, 8, 11, 1, -1, 6], 10), [11, -1])
    ]

    for case in test_cases:
        nums = case[0][0]
        value = case[0][1]
        print(f'{nums} {value}')

        result = target_sum(nums,value)
        print(f'result => {result} {case[1]}')
        assert(set(result) == set(case[1]))
