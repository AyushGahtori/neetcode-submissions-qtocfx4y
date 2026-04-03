from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()

            # both null → OK
            if not n1 and not n2:
                continue

            # one null → not same
            if not n1 or not n2:
                return False

            # values differ → not same
            if n1.val != n2.val:
                return False

            # push children as pairs
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True
