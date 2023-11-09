# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        
        def calcDepth(root, count):
            if not root:
                return count
            left,right = count,count
            if root.left:
                left = calcDepth(root.left,count+1)
            if root.right:
                right = calcDepth(root.right,count+1)
            return max(left,right)
        
        return calcDepth(root,1)
        