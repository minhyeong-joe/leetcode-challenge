# Leetcode Treenode structure and in,pre,postorder and leetcode representation of structure
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # inorder traversal list (left,self,right)
    def inorder(self):
        # recursive helper
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            traversal.append(node.val)
            dfs(node.right)

        traversal = list()
        dfs(self)
        return traversal

    # preorder traversal list (left,self,right)
    def preorder(self):
        # recursive helper
        def bfs(node):
            if not node:
                return

            traversal.append(node.val)
            bfs(node.left)
            bfs(node.right)

        traversal = list()
        bfs(self)
        return traversal

    # postorder traversal list (left,self,right)
    def postorder(self):
        # recursive helper
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            traversal.append(node.val)

        traversal = list()
        dfs(self)
        return traversal

    # leetcode representation of trees (level-by-level, and explicit None for absence of children)
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


# test driver
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, right=TreeNode(4)),
                    TreeNode(3, left=TreeNode(5, right=TreeNode(6))))
    print("inorder:", root.inorder())
    print("preorder:", root.preorder())
    print("postorder:", root.postorder())
    print("leetcode:", root)
