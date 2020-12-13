from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.traversal = list()

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.recursive(root)
        return self.traversal

    def recursive(self, root):
        if root is None:
            return

        self.recursive(root.left)
        self.recursive(root.right)
        self.traversal.append(root.val)


sol = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(sol.postorderTraversal(root))
