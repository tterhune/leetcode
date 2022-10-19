# -*- coding: utf-8 -*-

import random


def quicksort(items):
    if len(items) < 2:
        return items

    # Remove item at this location
    pivot_idx = random.randint(0, len(items)-1)

    # Removes item from this index
    pivot = items.pop(pivot_idx)
    print(f'pivot_idx = {pivot_idx} pivot = {pivot}')
    less_than = [i for i in items if i <= pivot]
    greater_than = [i for i in items if i > pivot]

    return quicksort(less_than) + [pivot] + quicksort(greater_than)


if __name__ == '__main__':
    test = [
        ([3, 1, 2, 8], [1, 2, 3, 8]),
        ([16, -8, 2, 99, 6], [-8, 2, 6, 16, 99]),
    ]

    for t in test:
        result = quicksort(t[0])
        print(f'result => {result}')
        assert result == t[1]
