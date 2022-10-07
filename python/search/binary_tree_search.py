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

def insert_node(root, node):
    print(f'Insert node: {node.value}')
    if root.value > node.value:
        if root.left is None:
            root.left = node
        else:
            insert_node(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            insert_node(root.right, node)

def create_bst():
    root = Node(4)

    nodes = []
    for i in range(1, 8):
        nodes.append(Node(i))

    insert_node(root, nodes[1])
    insert_node(root, nodes[5])
    insert_node(root, nodes[0])
    insert_node(root, nodes[2])
    insert_node(root, nodes[4])
    insert_node(root, nodes[6])

    return root

def print_tree(node):
    if node is None:
        return

    print(f'{node}')
    print_tree(node.left)
    print_tree(node.right)


if __name__ == '__main__':
    root = create_bst()
    print_tree(root)
