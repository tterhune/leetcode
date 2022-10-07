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


class Node:
    def __init__(self, value):
        # print(f'Create: {value}')
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        string = (f'NODE: {self.value}\n'
                 f'\tL: {self.left.value if self.left else "-"}'
                 f'\tR: {self.right.value if self.left else "-"}'
                  )
        return string


class Queue:
    def __init__(self):
        self.container = []

    def enqueue(self, item):
        # print(f'Queueing => {item.value}')
        self.container.append(item)

    def dequeue(self):
        if self.container:
            return self.container.pop(0)

    def empty(self):
        return self.container == []


class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        # print(f'Push => {item.value}')
        self.container.append(item)

    def pop(self):
        if self.container:
            return self.container.pop()

    def empty(self):
        return self.container == []


def build_tree():
    queue = Queue()

    i = 1
    n = Node(i)
    root = n

    queue.enqueue(n)
    while not queue.empty() and i <= 9:
        n = queue.dequeue()

        i += 1
        n.left = Node(i)
        queue.enqueue(n.left)

        i += 1
        n.right = Node(i)
        queue.enqueue(n.right)

    return root


def calc_depths_recurse(root, depth=0):
    if root is None:
        return 0

    return depth + calc_depths_recurse(root.left, depth+1) + calc_depths_recurse(root.right, depth+1)


def calc_depths(root):
    sum = 0
    stack = Stack()

    stack.push((root, 0))
    while not stack.empty():
        n = stack.pop()

        node = n[0]
        if node is None:
            continue

        depth = n[1]
        sum += depth
        stack.push((node.left, depth+1))
        stack.push((node.right, depth+1))
    return sum


def print_tree(node):
    if node is None:
        return

    print(f'{node}')
    print_tree(node.left)
    print_tree(node.right)


if __name__ == '__main__':
    root = build_tree()
    print_tree(root)
    sum = calc_depths(root)
    print(f'Sum of depth = {sum}')

    sum = calc_depths_recurse(root)
    print(f'Sum of depth recurse = {sum}')
