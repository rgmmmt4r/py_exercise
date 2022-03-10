
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) ->int:
        def count_depth(root):
            if root:
                return 1+ max(count_depth(root.left),count_depth(root.right))
            else:
                return 0
        return count_depth(root)
