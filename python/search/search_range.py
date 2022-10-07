
from typing import List

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109


class Solution:
    def binary_search(self, nums: List[int], value: int, start: int, end: int):
        if start > end:
            return -1

        mid = (end + start) // 2
        if value < nums[mid]:
            mid = self.binary_search(nums, value, start, mid - 1)
        elif value > nums[mid]:
            mid = self.binary_search(nums, value, mid + 1, end)
        return mid

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        length = len(nums)
        
        if not length:
            return ans
        
        index = self.binary_search(nums, target, 0, length-1)
        if index == -1:
            return ans
        
        end = index
        for i in range(index + 1, length):
            if nums[i] == target:
                end = i
            else:
                break
                
        start = index
        for i in range(index - 1, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break
                
        return [start, end]
