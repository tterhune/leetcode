# -*- coding: utf-8 -*-
##########################################################################
#
# Copyright (C) 2022 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
# The contents of this software are proprietary and confidential
# to the Hewlett Packard Enterprise Development LP.  No part of this
# program may be photocopied, reproduced, or translated into another
# programming language without prior written consent of the
# Hewlett Packard Enterprise Development LP.
#
##########################################################################

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
    sorted_list = insertion_sort([8, 5, 2, 3, 9, 7, 5, 1])
    print(f'{sorted_list}')

