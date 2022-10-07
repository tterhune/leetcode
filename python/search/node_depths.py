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

import collections

# Tell children depth
# if n == None: return 0
# f(n, d) = d + f(n.l, d+1) + f(n.r, d+1)

# iterative
# sum = 0
# stack: (1, 0)
# push (2, 1), (3, 1)
# pop (2, 1)
# push (4, 2), (5, 2)
# stack (4, 2), (5, 2), (3, 1)
# so long as nodes in stack, apply algorithm


class BinaryTree:
    def __init__(self, value):
        print(f'Create: {value}')
        self.value = value
        self.left = None
        self.right = None


def print_tree(node):
    if node == None:
        return

    print(f'Node: {node.value}')
    print_tree(node.left)
    print_tree(node.right)


def node_depths(root):
    pass


class Stack:
    def __init__(self):
        self.container = collections.deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        if self.container:
            return self.container.popleft()


if __name__ == '__main__':
    root = p = BinaryTree(0)
    c = 1

    s = Stack()
    for i in range(1, 11, 2):
        print(f'Adding node {i} and {i+1}')
        l = BinaryTree(i)
        r = BinaryTree(i+1)
        p.left = l
        p.right = r
        p = l if c % 2 == 0 else r
        c += 1

    print_tree(root)
    node_depths(root)
