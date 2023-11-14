# https://www.geeksforgeeks.org/find-level-maximum-sum-binary-tree/

class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def maximumSum(root):

    if root is None:
        return

    queue = []
    queue.append(root)

    result = queue[0].data

    while (len(queue) > 0):

        sum = 0
        count = len(queue)
        while (count > 0):
            node = queue.pop(0)

            sum = node.data + sum

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

            count -= 1

        result = max(result, sum)
    return result


root = Node(1)
root.left = Node(7)
root.right = Node(0)
root.left.left = Node(7)
root.left.right = Node(-8)
# root.right.right = Node(8)
# root.right.right.left = Node(6)
# root.right.right.right = Node(7)
print(maximumSum(root))
