# -*- coding: utf-8 -*-

def selection_sort(items):
    print(f'sorting: {items}')

    for i in range(len(items)):
        min_index = i

        # Find the smallest item in the remaining list
        # so that we can swap it with the one at index i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]

    return items


if __name__ == '__main__':
    test = [
        ([3, 1, 2, 8], [1, 2, 3, 8]),
        ([16, -8, 2, 99, 6], [-8, 2, 6, 16, 99]),
    ]

    for t in test:
        result = selection_sort(t[0])
        print(f'result => {result}')
        assert result == t[1]
