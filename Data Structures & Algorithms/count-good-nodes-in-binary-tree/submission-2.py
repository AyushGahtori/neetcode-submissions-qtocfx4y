class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 0
        stack = [(root, root.val)]  # (current_node, max_value_so_far)

        while stack:
            node, max_so_far = stack.pop()

            # Check if current node is good
            if node.val >= max_so_far:
                count += 1

            # Update max for children
            new_max = max(max_so_far, node.val)

            # Push children
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))

        return count
