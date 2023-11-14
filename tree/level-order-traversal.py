
# https://youtu.be/86g8jAQug04
# https://www.geeksforgeeks.org/level-order-tree-traversal/

class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def levelOrder(root):

    if root is None:
      return

    queue = []
    queue.append(root)

    while(len(queue)>0):
      print(queue[0].data)

      node = queue.pop(0)

      if node.left is not None:
          queue.append(node.left)

      if node.right is not None:
          queue.append(node.right)

root = Node(33)
root.left = Node(21)
root.right = Node(35)
root.left.left = Node(47)
root.left.right = Node(56)
levelOrder(root)


