# -*- coding: utf-8 -*-

# Power set is a set of all subsets of a set
#
# P(S) of {a, b, c} =
#       { {}, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c} }
#
# For a power set of size n, there are 2 ** n sets (exponential growth)
#       number of sets of sets = 2^n
#       when a new item is added, the number of sets doubles
#
# Each item added to the set, doubles the size of the power set
#
# Think of truth tables:
#   c b a
#   0 0 0 => {}
#   0 0 1 => {a}
#   0 1 0 => {b}
#   0 1 1 => {a, b}
#   1 0 0 => {c}
#   1 0 1 => {a, c}
#   1 1 0 => {b, c}
#   1 1 1 => {a, b, c}

def subsets2(nums):
    power_set = [[]]

    # for every item to add
    for n in nums:

        # for each list in our list
        for subset in power_set:

            # create a new list, that includes our new item, to each
            # list in our power set
            subset = subset + [n]

            # create a new list containing our list and add to power set
            power_set = power_set + [subset]

            print(f'n => {n} subset = {subset} power_set => {power_set}')

    return power_set


def subsets(nums):
    output = [[]]
    for n in nums:
        output += [o + [n] for o in output]
        print(f'n => {n} output => {output}')

    return output


if __name__ == '__main__':
    # result = subsets([1, 2, 3])
    result = subsets2([1, 2, 3])
    print(result)
