# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            rightside = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    rightside = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if rightside:        
                res.append(rightside.val)  
        return res              

        