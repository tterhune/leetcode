import heapq


def create_heap(items):
    print(f'Heapify: {items}')
    return heapq.heapify(items)


if __name__ == '__main__':
    test_cases = [
        ([88, 3, 100, 72, 12], []),
        ([-1, 10, 2, 30], []),
        ([16, -10, 8, 0, 200], []),
        ([11, 8, 99, 201], []),
    ]

    for case in test_cases:
        a = case[0]
        t = case[1]

        create_heap(a)
        print(f'Heap: => {a}')
        # assert result == r
