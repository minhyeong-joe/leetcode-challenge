# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def distributeCoins(self, root):
        self.actions = 0
        self.distributeDFS(root)
        return self.actions


    def distributeDFS(self, node):
        if node is None:
            return 0
        left = self.distributeDFS(node.left)
        right = self.distributeDFS(node.right)
        self.actions += abs(left) + abs(right)
        return node.val + left + right -1

solver = Solution()

leftNode = TreeNode(0)
rightNode = TreeNode(0)
root = TreeNode(3, leftNode, rightNode)
print(solver.distributeCoins(root))

leftNode = TreeNode(3)
rightNode = TreeNode(0)
root = TreeNode(0, leftNode, rightNode)
print(solver.distributeCoins(root))

leftNode = TreeNode(0)
rightNode = TreeNode(2)
root = TreeNode(1, leftNode, rightNode)
print(solver.distributeCoins(root))

root = TreeNode(1)
left = TreeNode(0)
right = TreeNode(0)
leftRight = TreeNode(3)
root.left = left
root.right = right
left.right = leftRight
print(solver.distributeCoins(root))

root = TreeNode(4, TreeNode(0, None, TreeNode(0, None, TreeNode(0))))
print(solver.distributeCoins(root))