from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        return str(self.val)

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        postOrder = list()
        stack = list()
        stack.append(root)
        while stack:
            currentNode = stack.pop()
            if currentNode.children is not None:
                stack.extend(currentNode.children) 
            postOrder.insert(0, currentNode.val)
        return postOrder


# test driver
sol = Solution()
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print("Output:", sol.postorder(tree))