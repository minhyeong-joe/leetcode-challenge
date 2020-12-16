from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def getAllElements(root1: TreeNode, root2: TreeNode) -> List[int]:
    # iterative
    # list1 = iterInorder(root1)
    # list2 = iterInorder(root2)

    # recursive
    list1 = list()
    list2 = list()
    recurInorder(root1, list1)
    recurInorder(root2, list2)
    result = list()
    i, j = 0, 0
    # merge two sorted lists
    while i < len(list1) and j < len(list2):
        if list1[i].val <= list2[j].val:
            result.append(list1[i].val)
            i+=1
        else:
            result.append(list2[j].val)
            j+=1
    for rem in list1[i:]:
        result.append(rem.val)
    for rem in list2[j:]:
        result.append(rem.val)
    return result

# Very slow. ~4284ms for Leetcode submission test cases
# Little bit less memory 17.1 MB for Leetcode submission test cases
def iterInorder(node: TreeNode):
    if node is None:
        return []
    stack = list()
    result = list()
    stack.append(node)
    while stack:
        print("Stack:", stack)
        print("Result:", result)
        # dig into left-most child
        while stack[-1].left is not None and stack[-1].left not in result:
            stack.append(stack[-1].left)
        # add left-most child to result
        nodeToAppend = stack.pop()
        result.append(nodeToAppend)
        if nodeToAppend.right is not None:
            stack.append(nodeToAppend.right)

    return result


# Much much faster ~400ms for Leetcode submission test cases
# Little bit more memory 20.3 MB for Leetcode submission test cases
def recurInorder(node: TreeNode, orderList):
    if node is None:
        return
    recurInorder(node.left, orderList)
    orderList.append(node)
    recurInorder(node.right, orderList)


# driver
# example 1
root1 = TreeNode(2, TreeNode(1), TreeNode(4))
root2 = TreeNode(1, TreeNode(0), TreeNode(3))
print("Input: root1 = [2,1,4], root2 = [1,0,3]")
print("Output:", getAllElements(root1, root2))

root1 = TreeNode(1, None, TreeNode(8))
root2 = TreeNode(8, TreeNode(1), None)
print("Input: root1 = [1,None,8], root2 = [8,1]")
print("Output:", getAllElements(root1, root2))

root1 = TreeNode(0, TreeNode(-10), TreeNode(10))
root2 = TreeNode(5, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(7))
print("Input: root1 = [0, -10, 10], root2 = [5, 1, 7, 0, 2]")
print("Output:", getAllElements(root1, root2))