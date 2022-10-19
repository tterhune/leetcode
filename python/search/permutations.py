# -*- coding: utf-8 -*-

# Permutations:
# - used when order of things in a list/set DO matter
# - think of a lock combination, order matters
#
#   [1, 2] != [2, 1]
#
# - two types:
#   - duplicates allowed
#   - duplicates NOT allowed
#
# Combinations:
# - used when order of things doesn't matter
# - think of a fruit salad
#
#   [1, 2] == [2, 1]
#

def permutations(items):
    return items


if __name__ == '__main__':
    result = permutations([1, 2, 3])
    print(result)
