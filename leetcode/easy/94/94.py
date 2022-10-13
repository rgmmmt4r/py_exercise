class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        answer = []
        def input_val(root: Optional[TreeNode]):
            cur = root
            if cur:
                input_val(cur.left)
                answer.append(cur.val)
                input_val(cur.right)
        input_val(root)

        return answer
