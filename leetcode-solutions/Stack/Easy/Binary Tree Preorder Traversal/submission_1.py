# Problem: Binary Tree Preorder Traversal
# Difficulty: Easy
# Topic: Stack
# Language: python
# Submission: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        mylist=[]
        if root is None:
            return mylist
        s=[root]
        while s:
            k=s.pop()
            mylist.append(k.val)
            if k.right:
                s.append(k.right)
            if k.left:
                s.append(k.left)
        return mylist

