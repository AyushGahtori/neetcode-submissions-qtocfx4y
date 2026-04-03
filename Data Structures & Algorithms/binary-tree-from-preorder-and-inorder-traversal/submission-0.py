class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])

            # Case 1: keep going left
            if stack[-1].val != inorder[inorderIndex]:
                stack[-1].left = node
                stack.append(node)

            # Case 2: backtrack and go right
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    last = stack.pop()
                    inorderIndex += 1

                last.right = node
                stack.append(node)

        return root
