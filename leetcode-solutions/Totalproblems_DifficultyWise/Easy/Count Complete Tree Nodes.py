# Count Complete Tree Nodes
# Difficulty: Easy
# Language: python

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        lh=0
        rh=0
        left=root
        right=root
        while left:
            lh+=1
            left=left.left
        while right:
            rh+=1
            right=right.right
        if lh==rh:
            return (1<<lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
