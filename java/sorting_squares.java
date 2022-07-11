
// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].
// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]
 

// Constraints:

// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums is sorted in non-decreasing order.

class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int [] a = new int[nums.length];
        int end_idx = nums.length - 1;
        int start_idx = 0;
        int a_idx = nums.length - 1; 
        
        // Work from both ends of the array since we know that those
        // are potentially the largest values.
        while (start_idx <= end_idx) {
            if (start_idx == end_idx) {
                a[a_idx] = end_sq;
                break;
            }

            int start = Math.abs(nums[start_idx]);
            int end = Math.abs(nums[end_idx]);
            
            if (start > end) {
                a[a_idx] = nums[start_idx] * nums[start_idx]; 
                start_idx++;
            } 
            else {
                 
                a[a_idx] = nums[end_idx] * nums[end_idx];
                end_idx--;
            }
            a_idx -= 1;
        }

        return a;
    }
}
