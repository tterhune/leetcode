# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [1, 3, 8, 9, 12, 14, 20, 21]

    index = binary_search(array, 23, 0, len(array) - 1)
    if index == -1:
        print('Not found')

    for i in range(0, 23):
        index = binary_search(array, i, 0, len(array) - 1)
        if index >= 0:
            print(f'Found {i} at: {index}')
            assert(array[index] == i)
        else:
            print(f'Didn\'t find: {i}')
