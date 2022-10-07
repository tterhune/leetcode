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


def valid_mountain(nums: List[int]) -> bool:
    array_len = len(nums)

    if array_len <= 2:
        return False

    right_highest = j = array_len - 1
    left_highest = i = 0

    for _ in range(0, array_len - 1):
        if nums[i] < nums[i + 1]:
            i += 1
            left_highest = i

        if nums[j] < nums[j - 1]:
            j -= 1
            right_highest = j

    if left_highest == 0 or right_highest == array_len - 1:
        return False

    if left_highest == right_highest:
        return True

    return False


if __name__ == '__main__':
    test_cases = [
        ([0, 3, 2, 1], True),
        ([4, 4, 3, 2, 1], False),
        ([1,1,1,1,1,1,1,2,1], False),
    ]

    for case in test_cases:
        nums = case[0]
        print(f'{nums}')

        result = valid_mountain(nums)
        print(f'result => {nums} {result}')
        assert(result == case[1])
