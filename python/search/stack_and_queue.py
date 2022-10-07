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


class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        print(f'Pushing: {item}')
        self.container.append(item)

    def pop(self):
        if self.container:
            return self.container.pop()


class Queue:
    def __init__(self):
        self.container = collections.deque()

    def enqueue(self, item):
        print(f'Queueing: {item}')
        self.container.append(item)

    def dequeue(self):
        if self.container:
            return self.container.popleft()


if __name__ == '__main__':
    s = Stack()
    for i in range(0, 4):
        s.push(i)

    for i in range(0, 4):
        item = s.pop()
        print(f'Stack popped: {item}')

    q = Queue()
    for i in range(0, 4):
        q.enqueue(i)

    for i in range(0, 4):
        item = q.dequeue()
        print(f'Queue dequeued: {item}')
