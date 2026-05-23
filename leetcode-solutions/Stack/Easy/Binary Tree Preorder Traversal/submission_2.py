# Problem: Binary Tree Preorder Traversal
# Difficulty: Easy
# Topic: Stack
# Language: python
# Submission: 2

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
        def preorder(root):
            if root is None:
                return
            mylist.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return mylist

