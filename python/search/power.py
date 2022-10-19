# -*- coding: utf-8 -*-

#
# Calculate a^b
#
def power(a, b):
    a_power = 1
    for i in range(1, b+1):
        a_power *= a
    return a_power


if __name__ == '__main__':
    test = [
        ([2, 4], 16),
        ([2, 1], 2),
        ([2, 0], 1),
        ([3, 3], 27),
        ([100, 0], 1),
        ([100, 1], 100),
        ([2, 8], 256),
    ]

    for t in test:
        a = t[0][0]
        b = t[0][1]
        result = power(a, b)
        print(f'{a}^{b} => {result}')
        assert result == t[1]
