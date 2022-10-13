# wrong answer
class Solution:
    depth = 0
    hist_depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.hist_depth = 0
        def inorder(root,depth):
            cur = root
            if cur:
                depth += 1
                inorder(cur.left)
                inorder(cur.right)
            else:
                if depth > self.hist_depth:
                    self.hist_depth = depth
        inorder(root,self.depth)
        return self.hist_depth