# Symmetric Tree
# Difficulty: Easy
# Language: python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def preorder(r1,r2):
            if not r1 and not r2 :
                return True
            elif not r1 or not r2 :
                return False
            elif r1.val!=r2.val:
                return False
            return preorder(r1.left,r2.right) and preorder(r1.right,r2.left)
        if not root:
            return True
        return preorder(root.left,root.right)
    

