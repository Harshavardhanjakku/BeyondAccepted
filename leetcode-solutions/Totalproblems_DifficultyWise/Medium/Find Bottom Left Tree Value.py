# Find Bottom Left Tree Value
# Difficulty: Medium
# Language: python

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q=deque([root])
        while q:
            node=q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val
            
