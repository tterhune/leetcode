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


def remove_dups(nums: List[int]) -> int:
    nums_len = len(nums)
    if nums_len <= 1:
        return nums_len

    # We know the number of elements >= 2

    # Use 2 pointer technique.

    # j tracks the non-duplicated values in the array
    # i will walk from the second element to the end
    # skip over elements that are the same.
    # once we hit a unique number, copy into the next open slot
    # as defined by j+1
    j = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[j]:
            # skip over
            continue
        else:
            j += 1
            nums[j] = nums[i]

    return j + 1


if __name__ == '__main__':
    test_cases = [
        ([1], 1),
        ([1, 1], 1),
        ([1, 1, 2], 2),
        ([1, 1, 2, 2], 2),
        ([2, 2, 3, 3, 4], 3),
        ([1, 2, 3, 3, 3, 4, 4, 5], 5),
    ]

    for case in test_cases:
        nums = case[0]
        print(f'{nums}')

        result = remove_dups(nums)
        print(f'result => {nums} {result}')
        assert(result == case[1])
