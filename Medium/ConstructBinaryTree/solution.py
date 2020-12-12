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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.recursiveBuild(0, 0, len(inorder), preorder, inorder)

    def recursiveBuild(self, preorderIndex: int, inorderStart: int, inorderEnd: int, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorderStart >= inorderEnd or preorderIndex >= len(preorder):
            return None
        node = TreeNode(preorder[preorderIndex])
        # find index of this node value at inorder
        inorderIndex = inorder.index(preorder[preorderIndex])
        # left node of current node is always next element in preorder (also pass in left subarray range)
        node.left = self.recursiveBuild(
            preorderIndex+1, inorderStart, inorderIndex, preorder, inorder)
        # right node of current node is current node + num of all left nodes + 1
        numLeftNodes = inorderIndex - inorderStart
        node.right = self.recursiveBuild(
            preorderIndex+numLeftNodes+1, inorderIndex+1, inorderEnd, preorder, inorder)
        return node


sol = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = sol.buildTree(preorder, inorder)

print(root)
