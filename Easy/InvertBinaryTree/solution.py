from utils import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case: if we hit null child
        if not root:
            return

        # swap left and right child
        temp = root.left
        root.left = root.right
        root.right = temp
        # traverse recursively
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


sol = Solution()
root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(
    3)), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))
# root = TreeNode(1)
# root = None
# root = TreeNode(1, TreeNode(2))
print("Before inversion:", root)

inverted = sol.invertTree(root)
print("Inverted Tree:", inverted)
