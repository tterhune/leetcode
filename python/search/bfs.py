# -*- coding: utf-8 -*-

from collections import deque


def bfs(graph, start_vertex):
    queue = deque()
    queue.append(start_vertex)
    visited = [start_vertex]

    while len(queue) > 0:
        vertex = queue.popleft()
        children = graph.get(vertex, [])

        for child in children:
            if child not in visited:
                print(f'adding: {child}')
                queue.append(child)
            else:
                print(f'already visited: {child}')

        visited.append(vertex)
        print(f'** visited: {vertex}')


if __name__ == '__main__':
    graph = {
        'tim': ['barbara', 'mark', 'allie', 'john', 'val'],
        'barbara': ['zoe', 'lucas'],
        'mark': ['ryan'],
        'allie': ['anna'],
        'john': ['lucas'],
        'val': ['summer'],
        'zoe': ['delaney'],
        'lucas': ['tim']
    }
    bfs(graph, 'tim')