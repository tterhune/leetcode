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

def func(i, s):
    print(f'in func({i}, {s})')
    if i == 0:
        return i
    s += 1
    i -= 1
    s += func(i, s)
    return s


if __name__ == '__main__':
    i = 10
    s = 0
    val = func(i, s)
    print(f'val = {val} s = {s}')
