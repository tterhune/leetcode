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

def delete_array2(nums: list, val: int) -> int:
    k = 0
    for i in nums:
        if i == val:
            continue
        nums[k] = i
        k += 1

    return k


def delete_array(nums: list, k: int) -> int:
    count = 0
    nums_len = len(nums)

    for i in range(nums_len - 1, -1, -1):
        if nums[i] == k:
            count += 1
            for j in range(i, nums_len - 1):
                nums[j] = nums[j + 1]

    return count


if __name__ == '__main__':
    test_cases = [
        (([1, 3, 3, 2], 3), 2),
        (([3, 2, 2, 3], 3), 2),
    ]

    for case in test_cases:
        nums = case[0][0]
        value = case[0][1]

        print(f'{nums} {value}')

        result = delete_array2(nums, value)
        print(f'{case[0]} = {result}')
        print(f'nums = {nums}')
        assert(result == case[1])
