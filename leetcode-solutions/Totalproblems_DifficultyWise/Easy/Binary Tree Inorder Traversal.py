# Binary Tree Inorder Traversal
# Difficulty: Easy
# Language: python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.myfunc(root,[])

    def myfunc(self, root,l):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root:
            self.myfunc(root.left,l)
            l.append(root.val)
            self.myfunc(root.right,l)
        return l
