# -*- coding: utf-8 -*-

def insertion_sort(array):
    # time  => O(n^2)
    # space => O(1)

    # Start at 1 since the first element is sorted
    # The second item, at index 1 is the first element to
    # insert in the sorted list
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            # swap
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array

if __name__ == '__main__':
    test = [
        ([3, 1, 2, 8], [1, 2, 3, 8]),
        ([16, -8, 2, 99, 6], [-8, 2, 6, 16, 99]),
    ]

    for t in test:
        result = insertion_sort(t[0])
        print(f'result => {result}')
        assert result == t[1]
