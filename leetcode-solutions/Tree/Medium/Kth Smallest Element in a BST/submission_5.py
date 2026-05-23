# Problem: Kth Smallest Element in a BST
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 5

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nums=[]
        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        inorder(root)
        return nums[k-1]
