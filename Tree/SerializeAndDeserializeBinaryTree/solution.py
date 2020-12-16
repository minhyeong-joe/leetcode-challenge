from typing import List

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
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


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorderList = list()
        self.preorder(root, preorderList)
        return(str(preorderList))

    def preorder(self, root, preorderList):
        if root is None:
            # if preorderList[len(preorderList)-1] is not None:
            preorderList.append(None)
            return
        preorderList.append(root.val)
        self.preorder(root.left, preorderList)
        self.preorder(root.right, preorderList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        return self.recursiveDeserialize(data)

    def recursiveDeserialize(self, data: List[int]) -> TreeNode:
        if len(data) <= 0:
            return
        currentVal = data.pop(0)
        if currentVal is None:
            return
        root = TreeNode(currentVal)
        root.left = self.recursiveDeserialize(data)
        root.right = self.recursiveDeserialize(data)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

sol = Codec()
# generate test tree [1,2,3,null,null,4,5]
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

print("Original Tree:", root)

ser = sol.serialize(root)
print("Serialization using preorder:", ser)
print("Deserialized tree:", sol.deserialize(ser))
