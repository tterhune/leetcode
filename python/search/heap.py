import heapq

def heap(array, target):
    pass

if __name__ == '__main__':
    test_cases = [
        ([0, 5, 10, 11, 120], []),
        ([-1, 1, 2, 30], []),
        ([-10, 0, 99, 200], []),
        ([1, 8, 99, 201], []),
    ]

    for case in test_cases:
        a = case[0]
        t = case[1]

        print(f'search for {t} in {a}')
        # result = binary_search(a, t)
        # assert result == r
