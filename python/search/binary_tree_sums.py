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


def print_tree(node):
    if node is None:
        return

    print(f'{node}')
    print_tree(node.left)
    print_tree(node.right)


def branch_sums(root):
    # Do a DFS, to do a DFS, we will use a stack or recursion
    stack = Stack()
    stack.push(root)

    sum = 0
    while not stack.empty():
        node = stack.pop()
        sum += node.value
        stack.push(node.left)
        stack.push(node.right)


if __name__ == '__main__':
    root = build_tree()
    # print_tree(root)
    branch_sums(root)

