


class Solution:
    result = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def look_depth(root) -> int:
            if not root:
                return 0
            left_height = look_depth(root.left)
            right_height = look_depth(root.right)
            if abs(left_height-right_height)>1:
                self.result = False
            return max(left_height,right_height)+1
        look_depth(root)
        return self.result