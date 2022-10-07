from collections import deque

class Queue:
    def __init__(self):
        self._nodes = deque()

    def enqueue(self, item):
        self._nodes.append(item)

    def dequeue(self):
        return self._nodes.popleft()

    def is_empty(self):
        return len(self._nodes) == 0


def nodeDepths(root):
    queue = Queue()

    level = 1
    if root.left is not None:
        queue.enqueue((root.left, level))

    if root.right is not None:
        queue.enqueue((root.right, level))

    sum = 0
    while not queue.is_empty():
        node_info = queue.dequeue()
        node = node_info[0]
        node_level = node_info[1]

        sum += node_level

        if node.left is not None:
            queue.enqueue((node.left, node_level + 1))

        if node.right is not None:
            queue.enqueue((node.right, node_level + 1))

    return sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    actual = nodeDepths(root)
    print(f'Actual: {actual}')
    assert actual == 16
