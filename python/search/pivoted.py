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

def binary_search(nums: List[int], value: int, start: int, end: int):
    if start > end:
        return -1

    mid = (start + end) // 2
    print(f'{start} -> {end} {mid}')
    if value < nums[mid]:
        mid = binary_search(nums, value, start, mid - 1)
    elif value > nums[mid]:
        mid = binary_search(nums, value, mid + 1, end)
    return mid

class Solution:

    def binary_search(self, nums: List[int], value: int, start: int, end: int):
        if start > end:
            return -1
        mid = (start + end) // 2
        if value < nums[mid]:
            mid = self.binary_search(nums, value, start, mid - 1)
        elif value > nums[mid]:
            mid = self.binary_search(nums, value, mid + 1, end)
        return mid

    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        index = - 1

        if nums[0] == 0:
            index = self.binary_search(nums, target, 0, length - 1)
        elif target < nums[0]:
            for i in range(length - 1, -1, -1):
                if nums[i] == target:
                    index = i
                    break

                if nums[i] == 0:
                    break
        else:
            for i in range(0, length):

                if nums[i] == target:
                    index = i
                    break

                if nums[i] == 0:
                    break

        return index


if __name__ == '__main__':
    c = Solution()
    answer = c.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(f'Answer = {answer}')
    assert(answer == 4)

    answer = c.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(f'Answer = {answer}')
    assert(answer == -1)

