from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        tree = list()
        queue = list()
        queue.append(self)
        while queue and not all(node is None for node in queue):
            currentNode = queue.pop(0)
            if currentNode is None:
                tree.append(None)
            else:
                tree.append(currentNode.val)
                queue.append(currentNode.left)
                queue.append(currentNode.right)
        return str(tree)


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1


sol = Solution()
tree1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
tree2 = TreeNode(2, TreeNode(1, right=TreeNode(4)),
                 TreeNode(3, right=TreeNode(7)))
print(tree1)
print(tree2)

mergedTree = sol.mergeTrees(tree1, tree2)

print(mergedTree)
