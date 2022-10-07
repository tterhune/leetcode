package main.java;

import java.util.Arrays;

// Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
// Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
// The tests are generated such that there is exactly one solution. You may not use the same element twice.
// Your solution must use only constant extra space.
// input = [2, 7, 11, 15] target = 9
// answer = [1,2]
public class TwoSum {
    public static int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;

        while (i < j) {
            if (numbers[i] + numbers[j] > target) {
                // If the number produced by the sum is > target, the larger value can't be part of
                // the sum.
                j--;
            } else if (numbers[i] + numbers[j] < target) {
                // If the number produced by the sum is < target, the smaller value can't be part of
                // the sum.
                i++;
            } else {
                break;
            }
        }

        return new int[]{i + 1, j + 1};
    }

    public static void main(String [] args) {
        int [] array = {2, 7, 11, 15};
        int [] answer = twoSum(array, 9);
        System.out.println(Arrays.toString(answer));
    }
}
