class Solution:
    result = False
    def isSymmetric(self, root) -> bool:
        def inorder(p,q):
            if p and q:
                inorder(p.left,q.left)
                if p.val != q.val:
                    self.result = False
                inorder(p.right,q.right)
            elif not p and q:
                self.result = False
            elif p and not q:
                self.result = False
        if root:
            inorder(root.left,root.right)
        else:
            return True
        return self.result
                