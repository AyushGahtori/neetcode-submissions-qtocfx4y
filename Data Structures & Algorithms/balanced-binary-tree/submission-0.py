class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            # base case
            if not node:
                return 0  # height = 0

            left = dfs(node.left)
            if left == -1:
                return -1  # left subtree unbalanced

            right = dfs(node.right)
            if right == -1:
                return -1  # right subtree unbalanced

            # check balance condition
            if abs(left - right) > 1:
                return -1

            # return height
            return 1 + max(left, right)

        return dfs(root) != -1
