# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -sys.maxsize, sys.maxsize)
    def helper(self, root:TreeNode, minimumB, maximumB) -> bool:
        if root is None:
            return True
        if root.val <= minimumB or root.val >= maximumB:
            return False
        return self.helper(root.left, minimumB,root.val) and self.helper(root.right,root.val,maximumB)
        
