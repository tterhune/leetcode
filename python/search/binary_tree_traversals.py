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
        string = (
            f'{self.value}'
            f' L: {self.left.value if self.left else "-"}'
            f' R: {self.right.value if self.right else "-"}'
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

def insert_tree(root, node):

    if root.value > node.value:
        if root.left is None:
            root.left = node
        else:
            insert_tree(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert_tree(root.right, node)

def create_bst():
    root = Node(4)
    nodes = []
    for i in range(1, 8):
        nodes.append(Node(i))

    root.left = nodes[1]
    root.right = nodes[5]

    nodes[1].left = nodes[0]
    nodes[1].right = nodes[2]

    nodes[5].left = nodes[4]
    nodes[5].right = nodes[6]

    return root

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


def in_order(node):
    # In order traversal means to "visit":
    # - the left branch
    # - the current node
    # - the right branch
    if node is None:
        return
    in_order(node.left)
    print(f'in_order: {node}')
    in_order(node.right)


def pre_order(node):
    # In pre-order traversal means to "visit":
    # - the current node
    # - the left branch
    # - the right branch
    if node is None:
        return
    print(f'pre_order: {node}')
    pre_order(node.left)
    pre_order(node.right)


def post_order(node):
    # In post-order traversal means to "visit":
    # - the left branch
    # - the right branch
    # - the current node
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f'post_order: {node}')


if __name__ == '__main__':
    # root = build_tree()
    root = create_bst()
    print_tree(root)
    in_order(root)
    pre_order(root)
    post_order(root)
