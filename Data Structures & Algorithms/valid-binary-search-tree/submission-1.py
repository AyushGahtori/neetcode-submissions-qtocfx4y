# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # assuming that if a second layer child node on the left has a child node on the right that is greater then the root node its still valid as log as all the greated values are on the right
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, low, high = stack.pop()
            if not(low < node.val < high):
                return False
            if node.right:
                stack.append((node.right, node.val, high))  
            if node.left:
                stack.append((node.left, low, node.val))  
        return True                                     


        